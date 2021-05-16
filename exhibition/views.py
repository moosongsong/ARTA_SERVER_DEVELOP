from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Exhibition, Category, Material, Piece, Comment, GuestBook, ExhibitionLike, PieceLike
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404


class SinglePage:
    def landing_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_main_page.html'
        )

    def about_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_introduction.html'
        )

    def login_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_User_members_login.html'
        )

    def test_page(request):
        return render(
            request,
            # add pages here
            'exhibition/ARTA_User_login.html'
        )


class ExhibitionList(ListView):
    model = Exhibition
    ordering = '-pk'
    paginate_by = 5
    template_name = 'exhibition/ARTA_User_exhibition_list.html'

    def get_context_data(self, **kwargs):
        context = super(ExhibitionList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['materials'] = Material.objects.all()
        return context


class ExhibitionDetail(DetailView):
    model = Exhibition

    template_name = 'exhibition/ARTA_User_exhibition_show.html'

    def get_context_data(self, **kwargs):
        context = super(ExhibitionDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class PieceDetail(DetailView):
    model = Piece

    template_name = 'exhibition/ARTA_User_piece_show.html'

    def get_context_data(self, **kwargs):
        context = super(PieceDetail, self).get_context_data()
        return context


class CommentManage:
    def new_comment(request, pk):
        if request.user.is_authenticated:
            piece = get_object_or_404(Piece, pk=pk)

            if request.method == 'POST':
                comment = Comment(content=request.POST.get('content'), piece=piece, user=request.user)
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(piece.get_absolute_url())
        else:
            return PermissionDenied

    def delete_comment(request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        piece = comment.piece
        if request.user.is_authenticated and request.user == comment.user:
            comment.delete()
            return redirect(piece.get_absolute_url())
        else:
            raise PermissionDenied


class GuestbookManage:
    def new_guestbook(request, pk):
        if request.user.is_authenticated:
            exhibition = get_object_or_404(Exhibition, pk=pk)

            if request.method == 'POST':
                guestbook = GuestBook(content=request.POST.get('content'), exhibition=exhibition, user=request.user)
                guestbook.save()
                return redirect(guestbook.get_absolute_url())
            else:
                return redirect(exhibition.get_absolute_url())
        else:
            return PermissionDenied

    def delete_guestbook(request, pk):
        guestbook = get_object_or_404(GuestBook, pk=pk)
        exhibition = guestbook.exhibition
        if request.user.is_authenticated and request.user == guestbook.user:
            guestbook.delete()
            return redirect(exhibition.get_absolute_url())
        else:
            raise PermissionDenied


class LikeManage:
    def exhibition_like(request, pk):
        if request.user.is_authenticated:
            exhibition = get_object_or_404(Exhibition, pk=pk)
            like = ExhibitionLike(exhibition=exhibition, user=request.user)
            like.save()
            return redirect(like.get_absolute_url())
        else:
            return PermissionDenied

    def exhibition_dislike(request, pk):
        like = get_object_or_404(ExhibitionLike, pk=pk)
        exhibition = like.exhibition
        if request.user.is_authenticated and request.user == like.user:
            like.delete()
            return redirect(exhibition.get_absolute_url())
        else:
            return PermissionDenied

    def piece_like(request, pk):
        if request.user.is_authenticated:
            piece = get_object_or_404(Piece, pk=pk)
            like = PieceLike(piece=piece, user=request.user)
            like.save()
            return redirect(like.get_absolute_url())
        else:
            return PermissionDenied

    def piece_dislike(request, pk):
        like = get_object_or_404(PieceLike, pk=pk)
        piece = like.piece
        if request.user.is_authenticated and request.user == like.user:
            like.delete()
            return redirect(piece.get_absolute_url())
        else:
            return PermissionDenied


class LikePage:
    def all_like_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_LikePage.html',
            {
                #
            }
        )


class PiecePage:
    def add_comment(request, pk):
        return render(
            request,
            'arta_front_develop/ARTA_User_piece_show.html',
            {
                #
            }
        )


class SearchPage:
    def search_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_search_page.html',
            {
                #
            }
        )

    def search_result_page(request, key):
        return render(
            request,
            'arta_front_develop/ARTA_search_result.html',
            {
                #
            }
        )
