[ work in progress ]  
middleware--中间件  
models--数据库model  
routes--路由  
static--图片等静态资源  
templates--模板  

###功能
首页、文章页、图片墙、留言 、自定义静态页 
文章详情页，带评论功能

后台管理

TODO:弹幕视频播放器

### 数据库

用户表
username,password,mail,phone,gender,role,created_at,deleted_at

文章表
title,content,class,user_id,visible,created_at,deleted_at

图片库表
path,thumbnail(可以不用这个字段),text,created_at

评论表
content,user_id,article_id,created_at,deleted_at
