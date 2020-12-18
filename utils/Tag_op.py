from bookmark.models import Tag


def tags_obj_save(tag_str):

    try:
        tag_lis = tag_str.split('#')
    except:
        return None
    tag_obj = []
    for tag in tag_lis:
        try:
            t = Tag.objects.get(name=tag)
            tag_obj.append(t)
        except:
            t = Tag()
            t.name = tag
            t.save()
            tag_obj.append(t)

    return tag_obj