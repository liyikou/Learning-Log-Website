# Learning Log

## Project Structure

LearningLog
│  .gitignore
│  db.sqlite3
│  manage.py
│  Readme.md
│  structure.txt
│
├─.vscode
│      launch.json
│      settings.json
│
├─learning_log
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │
│  └─__pycache__
│
├─learning_logs
│  │  admin.py
│  │  apps.py
│  │  forms.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  0002_entry.py
│  │  │  0003_topic_owner.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │
│  ├─static
│  │  └─learning_logs
│  │      ├─css
│  │      │      base.css
│  │      │
│  │      ├─image
│  │      │      beach.jpg
│  │      │      favicon.ico
│  │      │      NaturalGreen.jpeg
│  │      │
│  │      └─js
│  ├─templates
│  │  └─learning_logs
│  │          add_entry.html
│  │          add_topic.html
│  │          base.html
│  │          edit_entry.html
│  │          index.html
│  │          topic.html
│  │          topics.html
│  │
│  └─__pycache__
│
└─users
    │  admin.py
    │  apps.py
    │  models.py
    │  tests.py
    │  urls.py
    │  views.py
    │  __init__.py
    │
    ├─migrations
    │  │  __init__.py
    │  │
    │  └─__pycache__
    │
    ├─templates
    │  └─users
    │          login.html
    │          register.html
    │
    └─__pycache__

## Note

1. `conda create -n <env-name> python=3.10 django`
2. 创建根目录 .../LearningLog
3. 添加Readme.md
4. git仓库 设置
   1. Github 创建 New Repository
   2. `git remote add origin git@github.com:liyikou/Learning-Log-Website.git`
   3. `git add .\Readme.md`
   4. `git commit -m "docs: Add Readme.md"`
   5. `git branch -M main`
   6. `git push -u origin main`

    > **git 本地管理多个仓库**
    >
    > 在 Git 中设置不同项目使用不同的提交信息（用户名称和邮箱）是非常常见的需求。你可以为每个项目设置单独的用户信息。以下是如何为不同项目设置不同的用户信息：
    >
    > 1. 全局用户信息：
    >     首先，你可以设置全局的用户信息，这将被所有项目默认使用，除非在项目级别进行了覆盖设置。
    >
    >     ```bash
    >     git config --global user.name "Your Name"
    >     git config --global user.email "youremail@example.com"
    >     ```
    >
    > 2. 单个项目用户信息：
    >      在每个项目中，你可以设置单独的用户信息，这会覆盖全局设置。在项目目录中使用以下命令设置用户信息：
    >
    >      ```bash
    >      git config user.name "Project-specific Name"
    >      git config user.email "projectemail@example.com"
    >      ```
    >
    >   确保你在每个项目的根目录中设置项目特定的用户信息。这样，每个项目的提交将使用该项目特定的用户信息。
    >   要检查当前 Git 配置，可以使用以下命令：
    >
    > - 检查全局用户信息：`git config --global --list`
    > - 检查项目用户信息：`git config --list`
    >
    >
    > **Git Commit 规范**
    > 在 Git 中，采用规范化的提交消息格式有助于团队协作和代码维护的效率。一种流行的规范是使用 Conventional Commits 规范。>按照这个规范，一个提交消息被分成三个部分：Header、Body 和 Footer。
    >
    >  1. **Header**:
    >     - Header 包含一个类型、一个可选的作用域（scope），以及一个描述性的消息。格式为 `<type>(<scope>): ><description>`.
    >     - **Type**:
    >       - feat: 新功能（feature）
    >       - fix: 修复 bug
    >       - docs: 文档修改
    >       - style: 代码样式修改（不影响代码含义的变动，比如格式化）
    >       - refactor: 代码重构
    >       - test: 测试用例新增或修改
    >       - chore: 构建过程或辅助工具的变动
    >     - **Scope**：修改影响的范围（可选）
    >     - **Description**：对本次提交的简要描述
    >
    >  2. **Body**:
    >     - Body 是对 Header 进一步详细说明的部分，可以包含更多相关信息。
    >
    >  3. **Footer**:
    >     - Footer 可以包含一些关闭 issues 的信息或者是针对不兼容变动的说明。
    >
    >  例子：
    >
    >  ```plaintext
    >  feat(login): add social login options
    >
    >  This commit adds Google and Facebook login options to the login screen.
    >  Closes #123.
    >
    >  ```
    >
    >  遵循良好的提交规范有助于代码库的整洁性和可维护性。使用工具如 commitizen、Gitmoji 等可以帮助规范提交信息的格式。
5. 创建项目：`django-admin startproject learning_log .`
    不要忘记 `.`，否则创建的目录不对。
6. 迁移数据库创建Django基本表: `python manage.py migrate`
7. 创建Topic表
   1. `python manage.py makemigrations`
   2. `python manage.py migrate`
8. 创建超级用户：`python manage.py createsuperuser`
9. 设置Topic model的后台管理
10. 创建 Entry 表
11. `python manage.py shell`: 每次修改模型后，你都需要重启shell，这样才能看到修改的效果。要退出shell会话，可按Ctr + D；如果你使用的是Windows系统，应按Ctr + Z，再按回车键；如果是windows且安装了IPython，直接ctr + D，再按回车。
12. 创建 index page。
    1. 创建 index.html
        > 在文件夹learning_logs中新建一个文件夹，并将其命名为templates。在文件夹templates中，再新建一个文件夹，并将其命名为 learning_logs。这好像有点多余（我们在文件夹learning_logs中创建了文件夹templates，又在这个文件夹中创建了文件夹learning_logs），但建立了Django能够明确解读的结构，即便项目很大，包含很多应用程序亦如此。
    2. 在 view.py 创建 function
    3. 在 urls.py 添加 路由
    4. 在 项目总 urls.py 包含 learning_logs App 的路由
13. 创建并应用 base.html
14. 创建 Topics 页面
15. 添加 Topic 详情页
    1. `r'^topics/(?P<topic_id>\d+)/$'` 。`r` 让Django将这个字符串视为原始字符串，并指出正则表达式包含在引号内。这个表达式的第二部分`（/(?P<topic_id>\d+)/)` 与包含在两个斜杠内的整数匹配，并将这个整数存储在一个名为 `topic_id` 的实参中。这部分表达式两边的括号捕获URL中的值；`?P<topic_id>` 将匹配的值存储到 `topic_id` 中；而表达式 `\d+` 与包含在两个斜杆内的任何数字都匹配，不管这个数字为多少位。
    2. `topic(request, topic_id)` view要添上正则的参数。
16. 添加 Add Topic 功能
    1. forms--ModelForm
    2. request的属性
    3. forms初始化
    4. forms.is_valid()
17. Add Entry 功能
    1. "topic not found": 在短语“topic not found”中，确实没有明显的系动词（linking verb），但这并不影响短语的完整性和语法正确性。在这种情况下，谓语“not found”实际上是一个动词短语，动词“found”在这里充当实义动词，表示了主语“topic”状态的变化，即主题未被找到的状态。在英语语法中，有些表达方式可以在没有系动词的情况下完成句子，尤其是在简洁明了的短语或标题中。这种简洁的表达方式有时候更直接地传达信息，尤其当强调动作或状态的时候。由于这个短语是一个通用短语，所以它的简洁性有助于快速传达信息，省去了多余的词语，但在语法上仍然是合理和正确的。
18. Edit Entry 功能
    注意理解form的instance
19. 登录功能
    1. 创建users App: `python manage.py startapp users`
    2. 项目 settings 激活APP
    3. urls.py views.py login.html设计
    4. 主页设置根据 users.is_authenticated 显示不同信息
20. 注册功能
    用Django的UserCreationForm作表单校验账号密码格式是否合法，authenticate来校验账户密码是否正确，login为新用户创建有效的会话。
21. 添加登录限制
22. 将数据和用户关联，让用户只能访问自己的数据
    1. Topic关联User，迁移数据库，设置当前已有的主题的 owner 字段关联为 某User的id
        > `python manage.py flush`--重构数据库结构，但是所有的数据都会消失。
    2. Topics、Topic、edit_entry、new_entry界面添加关联和限制
23. 添加样式
    1. `pip install django-bootstrap3` or `conda install django-bootstrap3`
    2. 激活应用 INSTALLED_APPS 添加 'bootstrap'
        > 遇到bug：django.template.library.InvalidTemplateLibrary: Invalid template library specified. ImportError raised when trying to load 'bootstrap3.templatetags.bootstrap3': cannot import name 'Mapping' from 'collections' (e:\MyPythonEnvs\python3-12\Lib\collections\__init__.py)
        > 版本问题，我直接升级了 django-bootstrap 版本
    3. 让django-bootstrap3包含jQuery
        > 这是一个JavaScript库，让你能够使用Bootstrap模板提供的一些交互式元素;这些代码让你无需手工下载jQuery并将其放到正确的地方

        ```python
        BOOTSTRAP3 = {
            'include_jquery': True,
        }
        ```

    4. html文件 添加 `{% load bootstrap3 %}` 加载django-bootstrap3中的模板标签集; `{% bootstrap_css %}`加载css; `{% bootstrap_javascript %}` 加载js。
    5. 添加head和title,导航栏等样式
    6. 用bootstrap修改添加其他页面样式
    7. 添加favicon.ico和background
       1. 自己用link标签定义icon路径
       2. 写`route='/favicon'`重定向view
        > 注意：修改了代码一定要重启实例，然后强刷html页面，这样最保险，否则总会有样式应用不上的情况。
        > 关于django的静态文件配置和理解，看这些：
        > 1. <https://docs.djangoproject.com/zh-hans/5.0/intro/tutorial06/>
        > 2. <https://docs.djangoproject.com/zh-hans/5.0/howto/static-files/>
        > 3. <https://docs.djangoproject.com/zh-hans/5.0/ref/contrib/staticfiles/>
24. 将Django的User换成自定义User
    1. 继承AbstractUser，添加自定义字段
    2. settings.py 添加 `AUTH_USER_MODEL = 'users.User'`：设置用于权限认证的User到底是哪个。不指定这个会报UserPermission等表需要这个自定义User给AbstractUser关联的那些权限外键表新定义一个related name；指定后会报django.db.migrations.exceptions.InconsistentMigrationHistory这个错，因为0003_topic_owner这个字段用了AUTH_USER_MODEL指定的表，现在你换表了，相当于新加，但是你之前却已经根据AUTH_USER_MODEL指定的表生成过外键字段，那就不一致了。

    解决办法：
    一、重来一遍
       1. 删掉所有migration文件
       2. 删掉数据库所有数据
       3. `python manage.py makemigrations`
       4. `python manage.py migrate`

    二、找问题解决问题
       报错其实就是owner字段的问题。
       5. 先把所有添加User修改Topic的代码直接`git stash`一下，让代码回到之前的状态
       6. 直接migrate 到这个migration上一个，0002_entry.py：`python manage.py migrate learning_logs 0002`(这会儿你的owner字段和对应字段的数据都没了)，然后删除掉0003_topic_owner.py文件
       7. pop latest stash，把代码应用回来
       8. 然后重新跑 users 的 migrations:`python manage.py makemigrations users`、`python manage.py migrate`（这会儿你之前的User数据都没了）
       9. 新建一个User：`python manage.py createsuperuser` （用于后面 owner字段的默认值）
       10. 然后重新跑 learning_logs 的 migrations:`python manage.py makemigrations learning_logs` （中间提示的时候选择指定默认值，然后输入`1`就行——你也可以自己多创建几个，然后输入那个User的Id）、`python manage.py migrate learning_logs`大功告成！
25. 修改了Topic的字段名字，修改对应调用地方

## Bugs

1. `{% form.as_p %}`
    注意`{%%}`是标签，不是`{{}}`
2. add entry界面多出了topic.html的东西？一点击就跳转？？
    `<a>`没有闭合。

## Else

1. 发现 git commit 的email是关联 Github的主要元素，关联上GitHub之后commit info就会显示头像。

## Todo

1. 手机号发送验证码注册
2. 关联qq，微信号
3. 忘记密码功能
4. 确保任何用户都可访问所有的博文，但只有已登录的用户能够发表博文以及编辑既有博文。
5. 删除Topic，Entry功能
