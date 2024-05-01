[README](https://xn--zsr428b1mg.com/2024/05/01/README/)
## 安装Hexo

> Hexo官网：https://hexo.io/zh-cn/

### 1. 创建项目文件夹（根目录）

### 2. 进入项目文件夹

### 3. 打开Git Bush Here(以下简称为GBH)

### 4. 安装hexo

```bash
npm install hexo-cli -g
hexo init blog
cd blog
npm install
hexo server
```

> server可缩写成s  
> GBH中Ctrl+C为关闭服务
> 默认本地展示地址：http://localhost:4000/ 

## 创建博客

### 1. 进入项目文件夹

### 2. 打开GBH

### 3. 新建文章

```bash
hexo new "title"
```

### 4. 进入"\Source\_posts"即可看到文章

## 配置文章

### 1. 生成网页

```bash
hexo generate
```

> generate可缩写成g

### 2. 运行博客

```bash
hexo server
```

> server可缩写成s 

### 3. 查看博客

- http://localhost:4000/ 



### 4. 上传博客

```bash
hexo deploy
```

> deploy可缩写成d

### 后续更新维护流程

1. **新建文章**
    `hexo new "title"`
2. **编辑文章**
3. **生成网页**
    `hexo g`
4. **检查网页（可省）**
    `hexo s`
5. **上传博客到仓库（需要获取密钥 配置连接）**
    `hexo d `





