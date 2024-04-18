# djangorestframework-admin

## 介绍
基于DRF开发的后台管理

## 原则
### 模块依赖

### 搜索限制
1. 被依赖对象不能根据依赖对象过滤
   比如角色依赖用户，那用户就不能根据角色进行搜索；

### 删除限制
1. 删除上级时默认解除与下级的关联；
2. 删除下级时需要先解除与上级的关联；


### 权限管理
* 整体区分为两种类型
  * 应用类型：适用于管理的角度，仅分为
    * 创建者
    * 管理员
    * 用户
  * 业务类型：适用于业务的角度，具体需要业务区分

### API管理区分
1. 主要分两种类型：
   * 管理端，RESTFUL风格，
   * 用户端，仅限于搜索（即list）使用的是RESTFUL风格，后缀me；比如：
     * 我创建的
     * 我加入的
     * ……
2. 示例
  * 用户组列表
    * 管理端是`user/groups`
    * 用户端是`user/me/groups/`
  * 租户列表
    * 管理端`tenant/tenants`
    * 用户端
      * 所有`tenant/me/tenants`
      * 我创建的`tenant/me/tenants/owned`
      * 我加入的`tenant/me/tenants/joined`


## 软件架构
软件架构说明
* auth，身份认证与管理模块
  * jwt，基于JWT的登录与校验
  * model，基于models.Model的登录
* user，用户管理
  * group, 用户组
* role，角色管理
  * permission，权限管理（RBAC模型）
  
* static，静态资源
  * swagger-ui，swagger文档的静态资源
* system，系统配置管理模块

## 使用
1. 新建DRF项目（以`backend`为例）；
2. 安装
3. 重置配置文件
  ```shell
  cd backend/backend
  mv settings.py default_settings.py
  cp .../rest_framework_admin/template/settings.py ./
  cp .../rest_framework_admin/template/urls.py ./
  ```
4. 根据需要更新

