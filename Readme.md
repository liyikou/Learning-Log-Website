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
