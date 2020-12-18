# -*- coding:utf-8 -*-
from django.shortcuts import render, reverse, redirect
from utils.import_bookmarks import BookmarksTodb
from bookmark.models import BookmarkForm, Bookmark, Tag
from django.http import HttpResponse
from django.views.generic import View

import json
# Create your views here.


def index(request):
    bf_list = BookmarkForm.objects.all()
    return render(request, 'index.html', {'list': bf_list, 'sign': 'folder'})

class FolderAddView(View):
    '''文件夹新增或修改'''

    def get(self, request):
        return render(request, 'folder_add.html')

    def post(self, request):
        folder_name = request.POST.get('folder_name')
        desc = request.POST.get('desc')
        if not all([folder_name]):
            return render(request, 'folder_add.html', {'errmsg': '请输入文件名'})
        bf = BookmarkForm()
        bf.folder_name = folder_name
        bf.desc = desc
        bf.save()
        return redirect(reverse('folder:index'))

class FolderEditView(View):
    '''文件夹新增或修改'''

    def get(self, request):
        cage = request.GET.get('cage')
        bf = BookmarkForm.objects.get(id=cage)
        return render(request, 'folder_edit.html', {'bf':bf})

    def post(self, request):
        folder_name = request.POST.get('folder_name')
        desc = request.POST.get('desc')
        folder_id = request.POST.get('folder_id')

        if not all([folder_name, folder_id]):
            return redirect(reverse('folder:index'))

        try:
            bf = BookmarkForm.objects.get(id=folder_id)
        except BookmarkForm.DoesNotExist:
            bf = BookmarkForm()
        bf.folder_name = folder_name
        bf.desc = desc
        bf.save()
        return redirect(reverse('folder:index'))

class BookmarkView(View):
    def get(self, request):
        folder_id = request.GET.get('folder_id')

        if not all([folder_id]):
            return redirect(reverse('folder:index'))
        bf = BookmarkForm.objects.get(id=folder_id)
        bm_lis = Bookmark.objects.filter(folder__id=folder_id).all()
        return render(request, 'list.html', {'bf': bf,  'list': bm_lis})


class FolderDelteView(View):
    def post(self, request):
        resp = {'code': 200, 'msg': '操作成功', 'data': {}}
        id = request.POST.get('id')
        act = request.POST.get('act')
        if not all([id, act]):
            resp['code'] = -1
            resp['msg'] = '数据不完整'

        bf = BookmarkForm.objects.get(id=id)
        bf.delete()
        return HttpResponse(json.dumps(resp))


class TagView(View):
    def get(self, request):
        tag_list = Tag.objects.all()
        return render(request, 'tags.html', {'sign': 'tag', 'list': tag_list})

    def post(self, request):
        resp = {'code': 200, 'msg': '操作成功', 'data': {}}
        id = request.POST.get('id')
        act = request.POST.get('act')
        if not all([id, act]):
            resp['code'] = -1
            resp['msg'] = '数据不完整'

        tag = Tag.objects.get(id=id)
        tag.delete()
        return HttpResponse(json.dumps(resp))




class TagAddView(View):

    def post(self, request):
        tag_name = request.POST.get('tag_name')
        if not all([tag_name]):
            return redirect(reverse('folder:tag'))
        tag = Tag()
        tag.name = tag_name
        tag.save()
        return redirect(reverse('folder:tag'))

class TagEditView(View):

    def post(self, request):
        tag_name = request.POST.get('tag_name')
        tag_id = request.POST.get('tag_id')

        if not all([tag_name, tag_id]):
            return redirect(reverse('folder:tag'))
        tag = Tag.objects.get(id=tag_id)
        tag.name = tag_name
        tag.save()
        return redirect(reverse('folder:tag'))
