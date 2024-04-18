# Django
from django.contrib.contenttypes.models import ContentType

# Third party
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.page import get_page_from_request
from cms.utils.urlutils import admin_reverse

# Local application / specific library imports
from .conf.settings import (
    SIMPLE_NOTES_CUSTOM_CONTENT_TYPE_AND_ID,
    SIMPLE_NOTES_TOOLBAR_EDIT_TEXT,
    SIMPLE_NOTES_TOOLBAR_LIST_TEXT,
    SIMPLE_NOTES_TOOLBAR_MENU_TEXT,
)
from .models import SimpleNote


def get_content_type_and_id(request):
    """get contenttype + object id for each "type" of page (apphooks pages, then in last regular djangocms pages)"""

    object_ct, object_id = False, False
    found = False
    if SIMPLE_NOTES_CUSTOM_CONTENT_TYPE_AND_ID:
        # returns False, False if nothing is found
        object_ct, object_id = SIMPLE_NOTES_CUSTOM_CONTENT_TYPE_AND_ID(request)
        if object_ct is not None and object_id is not None:
            found = True

    if not found:
        # djangocms blog post (not the homepage of the blog, which should be treated as a regular cms page)
        if (
            request.resolver_match
            and request.resolver_match.app_name == "djangocms_blog"
            and "slug" in request.resolver_match.kwargs
        ):
            # Third party
            from djangocms_blog.models import Post

            try:
                post = Post.objects.get(
                    translations__slug=request.resolver_match.kwargs["slug"],
                    translations__language_code=request.LANGUAGE_CODE,
                )
                object_ct = Post
                object_id = post.id
            except Post.DoesNotExist:
                pass
        # regular cms pages

        elif (
            request.resolver_match
            and "slug" in request.resolver_match.kwargs
            and request.resolver_match.kwargs["slug"] == ""
        ):
            # Third party
            from cms.models import Page

            # homepage
            # if using multiple sites
            if getattr(request, "site", False):
                page = Page.objects.get(
                    title_set__language=request.LANGUAGE_CODE,
                    title_set__publisher_is_draft=False,
                    is_home=True,
                    node__site=request.site,
                )
            else:
                page = Page.objects.get(
                    title_set__language=request.LANGUAGE_CODE,
                    title_set__publisher_is_draft=False,
                    is_home=True,
                )
            object_ct = Page
            object_id = page.id
        else:
            # Third party
            from cms.models import Page

            # regular page
            if request.resolver_match and "slug" in request.resolver_match.kwargs:
                slug = request.resolver_match.kwargs["slug"].split("/")[-1]
            else:
                if request.resolver_match:
                    slug = request.resolver_match.route.split("/")
                    if slug[-1] == r"\Z":
                        slug = slug[-2]
                    else:
                        slug = slug[:-1]

                    if type(slug) is list and len(slug) > 1:
                        slug = slug[-1]
                else:
                    slug = None

            object_ct = None
            object_id = None
            try:
                page = get_page_from_request(request, clean_path=True)
                if page is None:  # not a cms page
                    # if using multiple sites
                    if getattr(request, "site", False):
                        page = Page.objects.filter(
                            title_set__language=request.LANGUAGE_CODE,
                            title_set__publisher_is_draft=False,
                            title_set__slug=slug,
                            node__site=request.site,
                        )
                    else:
                        page = Page.objects.filter(
                            title_set__language=request.LANGUAGE_CODE,
                            title_set__publisher_is_draft=False,
                            title_set__slug=slug,
                        )
                    page = page[0] if page.exists() else None
                if page is not None:
                    object_ct = Page
                    object_id = page.id
            except Page.DoesNotExist:
                pass

    if object_ct is not None:
        object_ct = ContentType.objects.get_for_model(object_ct)

    return (object_ct, object_id)


def get_edit_link(request):
    """
    Edit link will create an empty note if no one if found, and return the change url. That way, no need to reload the url in the toolbar!
    """
    ct, id = get_content_type_and_id(request)
    if ct and id:
        try:
            # if using multiple sites
            if getattr(request, "site", False):
                note = SimpleNote.objects.get(
                    content_type=ct,
                    object_id=id,
                    language_code=request.LANGUAGE_CODE,
                    site=request.site,
                )
            else:
                note = SimpleNote.objects.get(
                    content_type=ct, object_id=id, language_code=request.LANGUAGE_CODE
                )
            return admin_reverse(
                "django_simple_notes_simplenote_change", args={note.id}
            )
        except SimpleNote.DoesNotExist:
            note = SimpleNote(
                content_type=ct,
                object_id=id,
                language_code=request.LANGUAGE_CODE,
                author=request.user,
            )
            if getattr(request, "site", False):
                note.site = request.site
            note.save()
            return admin_reverse(
                "django_simple_notes_simplenote_change", args={note.id}
            )
    return None


@toolbar_pool.register
class SimpleNoteToolbar(CMSToolbar):
    watch_models = [SimpleNote]

    def populate(self):

        notes_menu = self.toolbar.get_or_create_menu(
            key="simple_notes_cms_integration",
            verbose_name=SIMPLE_NOTES_TOOLBAR_MENU_TEXT,
        )

        edit_link = get_edit_link(self.request)

        if edit_link:
            notes_menu.add_sideframe_item(
                name=SIMPLE_NOTES_TOOLBAR_EDIT_TEXT, url=edit_link
            )

        notes_menu.add_sideframe_item(
            name=SIMPLE_NOTES_TOOLBAR_LIST_TEXT,
            url=admin_reverse("django_simple_notes_simplenote_changelist"),
        )
