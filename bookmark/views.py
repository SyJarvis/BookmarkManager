from django.shortcuts import render, reverse, redirect
from utils.import_bookmarks import BookmarksTodb
from bookmark.models import BookmarkForm, Bookmark, Tag
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
import json
from utils.Tag_op import tags_obj_save
# Create your views here.



class BookmarkAddView(View):
    '''书签新增或修改'''
    def get(self, request):

        return render(request, 'bookmark_add.html')

    def post(self, request):
        url = request.POST.get('url')
        title = request.POST.get('title')
        folder_name = request.POST.get('folder_name')
        tags = request.POST.get('tags')
        desc = request.POST.get('desc')

        if not all([url, title, folder_name]):
            return render(request, 'bookmark_add.html', {'errmsg':'数据不完整'})

        try:
            bf = BookmarkForm.objects.get(folder_name=folder_name)
            print(bf)
        except:
            return render(request, 'bookmark_add.html', '请填写分类')
        tag_lis = tags_obj_save(tags)
        # 标签处理

        bm = Bookmark()
        bm.url = url
        bm.website_title = title
        bm.folder = bf
        bm.desc = desc
        bm.save()

        # 标签
        for tag in tag_lis:
            bm.tags.add(tag)
            bm.save()

        return redirect(reverse('folder:index'))


class BookmarkEditView(View):

    def get(self, request):
        folder_id = request.GET.get('folder_id', '')
        bm_id = request.GET.get('bm_id')
        print(bm_id)
        bm_id = int(bm_id)
        if not bm_id:
            return HttpResponseRedirect('/list?folder_id=%s'%folder_id)
        try:
            bm = Bookmark.objects.get(id=bm_id)
        except Bookmark.DoesNotExist:
            return render(request, 'bookmark_add.html')
        tags = bm.tags.all()
        print(tags)
        tags = [tag.name for tag in tags]
        print(tags)
        tags_str = '#'
        tags_str = tags_str.join(tags)
        print(tags_str)

        return render(request, 'bookmark_edit.html', {'bm':bm, 'tags_str': tags_str})

    def post(self, request):
        url = request.POST.get('url')
        title = request.POST.get('title')
        folder_name = request.POST.get('folder_name')
        bookmark_id = request.POST.get('bookmark_id')
        folder_id = request.POST.get('folder_id')
        tags = request.POST.get('tags')
        desc = request.POST.get('desc')
        print(folder_name)

        try:
            bf = BookmarkForm.objects.get(id=folder_id)
        except:
            return redirect(reverse('folder:index'))

        if not all([url, title, folder_name, bookmark_id]):
            return HttpResponseRedirect('/list?folder_id=%s'%bf.id)
        tag_lis = tags_obj_save(tags)
        try:
            bm = Bookmark.objects.get(id=bookmark_id)
            bm.url = url
            bm.website_title = title
            bm.folder = bf
            bm.desc = desc
            # 标签
            # 标签
            for tag in tag_lis:
                bm.tags.add(tag)

            bm.save()
            bm.save()
        except:
            redirect(reverse('folder:index'))

        return HttpResponseRedirect('/list?folder_id=%s'%bf.id)


class BookmarkDelteView(View):

    def post(self, request):
        resp = {'code': 200, 'msg': '操作成功', 'data': {}}
        id = request.POST.get('id')
        print(id)
        act = request.POST.get('act')
        if not all([id, act]):
            resp['code'] = -1
            resp['msg'] = '数据不完整'

        bm = Bookmark.objects.get(id=id)
        bm.delete()
        return HttpResponse(json.dumps(resp))

class BookmarkView(View):
    def get(self, request):
        bm_list = Bookmark.objects.all()

        return render(request, 'bookmarks.html', {'list': bm_list, 'sign':'bookmark'})