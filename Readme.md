# Learning Log

## Project Structure

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

## Bugs

1. `{% form.as_p %}`
    注意`{%%}`是标签，不是`{{}}`
2. add entry界面多出了topic.html的东西？一点击就跳转？？
    `<a>`没有闭合。

## Else

1. 发现 git commit 的email是关联 Github的主要元素，关联上GitHub之后commit info就会显示头像。
