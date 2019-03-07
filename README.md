部署到pythonanywhere注意修改setting.py
git pull更新

ALLOWED_HOSTS = [u'janyroo.pythonanywhere.com']

MEDIA_ROOT = u'/home/janyroo/to_do_list/todolist/media'
MEDIA_URL = '/media/'
STATIC_ROOT = u'/home/janyroo/to_do_list/todolist/static'
STATIC_URL = '/static/'



成功修复
Failed to find a valid digest in the 'integrity' attribute for resource '
**/css/bootstrap.min.css' with computed SHA-256 integrity 'nvT75FkXevX06WR8vlhFFP02xzhq9qFxLQOuS0LkWyQ='. 
The resource has been blocked.

去掉：

integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous"

"anonymous"

会发起一个跨域请求(即包含 Origin: HTTP 头). 但不会发送任何认证信息 (即不发送 cookie, X.509 证书和 HTTP 基本认证信息). 如果服务器没有给出源站凭证 (不设置 Access-Control-Allow-Origin: HTTP 头), 这张图片就会被污染并限制使用.

integrity 

包含行内元数据，它是一个你用浏览器获取的资源文件的哈希值，以base64编码的方式加的密，这样用户能用它来验证一个获取到的资源,在传送时未被非法篡改，详情查看Subresource Integrity。


2019-3-8
修复了秒表末开始时,点击提交会加入大量时间
    if b>1051982140862:
        b=0
 如果时间大于1051982140862说时没有点开始就 点提交,因为点开始后时间不可能大于这个数,这个数是1970年到现在的数
 
 
 修复了秒表和按扭总是第一行才有效
 在点击按扭()和按扭id上加入了键值变量,成功定位