---
title: 垃圾代码编写指南_C语言版
date: 2025-03-10 17:23:00
tags: 其他
---
## 前言

作为一名程序员，通常都需要跟别人协作编写代码。https://github.com/trekhleb/state-of-the-art-shitcode 是一个教你如何编写 💩 代码的教程，但是这个教程的代码示例是用 JavaScript 编写的，在本文我将其转成了经典的C语言，并且将一些语言风格写成符合中国程序员的编码习惯

## 代码编写原则

### 💩 定义变量的时候，尽可能用混淆的方式

变量命名的时候尽可能写短，能节省敲代码的时间

正确做法 👍🏻

```c
int a = 42;
```

错误做法 👎🏻

```c
int age = 42;
```

### 💩 采用变量/函数的混合命名风格

命名风格要采取多样化，彰显个人魅力

正确做法 👍🏻

```c
int wWidth = 640;
int w_height = 480;
```

错误做法 👎🏻

```c
int windowWidth = 640;
int windowHeight = 480;
```

### 💩 永远不要写注释

程序员最讨厌的两件事是：

1. 别人的代码不写注释
2. 别人让自己给代码写注释

正确做法 👍🏻

```c
const int cdr = 700;
```

错误做法 👎🏻

注释应该包含一些"为什么"而不是"做了什么"。如果代码中的"做了什么"不清楚，那么代码可能太混乱了。

```c
// 700ms的数量是根据UX A/B测试结果进行经验计算的。
// @查看: <详细解释700的一个链接>
const int callbackDebounceRate = 700;
```

### 💩 尽量用母语写注释

中国人写注释当然要用中文，怎么可能用英语这种通用语言，当然是怎么爽怎么来

正确做法 👍🏻

```c
// 错误时隐藏模态窗口。
closeModal(0);
```

错误做法 👎🏻

```c
// Hide modal window on error.
closeModal(0);
```

### 💩 尽可能混合各种格式风格

跟上述变量命名的原则一样，保持个性化~

正确做法 👍🏻

```c
char* i[] = {"tomato", "onion", "mushrooms"};
char* d[] = { "ketchup", "mayonnaise" };
```

错误做法 👎🏻

```c
char* ingredients[] = {"tomato", "onion", "mushrooms"};
char* dressings[] = {"ketchup", "mayonnaise"};
```

### 💩 把代码都写到一行

正确做法 👍🏻

```c
void parse_url_params(char* url, char* params) { char* p=strstr(url,"?");if(!p)return;p++;char* token=strtok(p,"&");while(token!=NULL){char* eq=strchr(token,'=');if(eq){*eq='\0';strcat(params,token);strcat(params,"=");strcat(params,eq+1);strcat(params,";");}token=strtok(NULL,"&");}}
```

错误做法 👎🏻

```c
void parse_url_params(char* url, char* params) {
    // Find the '?' character
    char* p = strstr(url, "?");
    if (!p) return;
  
    // Skip the '?' character
    p++;
  
    // Parse each parameter
    char* token = strtok(p, "&");
    while (token != NULL) {
        char* eq = strchr(token, '=');
        if (eq) {
            // Separate key and value
            *eq = '\0';
            strcat(params, token);
            strcat(params, "=");
            strcat(params, eq + 1);
            strcat(params, ";");
        }
        token = strtok(NULL, "&");
    }
}
```

### 💩 不要做异常处理

程序中任何可能出现异常的代码片段，没必要去捕捉，也不要写日志进行记录，更不要弹出啥错误提示，让你的协作者自己猜可能的报错原因就好了

正确做法 👍🏻

```c
FILE* file = fopen("important.dat", "r");
if (file == NULL) {
    // tss... 🤫
}
```

错误做法 👎🏻

```c
FILE* file = fopen("important.dat", "r");
if (file == NULL) {
    perror("Error opening file");
    // and/or
    log_error("Failed to open important.dat");
}
```

### 💩 大量使用全局变量

吕蒙过江，我也过江，别的函数能使用的变量，我为什么不能访问到？所以要多使用全局变量

正确做法 👍🏻

```c
int x = 5;

void square() {
    x = x * x;
}

int main() {
    square(); // Now x is 25.
    return 0;
}
```

错误做法 👎🏻

```c
int x = 5;

int square(int num) {
    return num * num;
}

int main() {
    x = square(x); // Now x is 25.
    return 0;
}
```

### 💩 多创建一些用不到的变量

以备不时之需。

正确做法 👍🏻

```c
int sum(int a, int b, int c) {
    const int timeout = 1300;
    const int result = a + b;
    return a + b;
}
```

错误做法 👎🏻

```c
int sum(int a, int b) {
    return a + b;
}
```

### 💩 如果你的编程语言允许，不要指定类型和/或不做类型检查

代码跑的怎样你别管，你就说能不能跑吧

正确做法 👍🏻

```c
void* sum(void* a, void* b) {
    // 不做类型检查，直接转换并希望一切顺利
    return (void*)((long)a + (long)b);
}
    // 在这里尽情享受无拘无束的乐趣
int main() {
    char* result1 = sum("hello", "world");  // 未定义行为
    int result2 = (int)sum((void*)5, (void*)10);  // 可能行得通？
    return 0;
}
```

错误做法 👎🏻

```c
int sum(int a, int b) {
    return a + b;
}

int main() {
    int result = sum(5, 10);  // 类型安全，意图明确
    return 0;
}
```

### 💩 你需要有一段永远无法执行到的代码

没想到吧 jojo 这就是我的逃跑路线！

正确做法 👍🏻

```c
int square(int num) {
    if (num == 0) {
        return 0;
    }
    else {
        return num * num;
    }
    return -1; // 这就是我的逃跑路线哒！哈哈哈
}
```

错误做法 👎🏻

```c
int square(int num) {
    if (num == 0) {
        return 0;
    }
    return num * num;
}
```

### 💩 三角形原则

像鸟一样筑巢，一层又一层。

正确做法 👍🏻

```c
void someFunction() {
    if (condition1) {
        if (condition2) {
            beginAsyncOperation(params, callback);
            if (callbackCalled) {
                if (result) {
                    for (;;) {
                        if (condition3) {
                            // 代码逻辑
                        }
                    }
                }
            }
        }
    }
}
```

错误做法 👎🏻

```c
void someFunction() {
    if (!condition1 || !condition2) {
        return;
    }
  
    beginAsyncOperation(params, callback);
    if (!callbackCalled || !result) {
        return;
    }
  
    for (;;) {
        if (condition3) {
             // 代码逻辑
        }
    }
}
```

### 💩 搞乱缩进

避免使用缩进，因为它们会使复杂的代码在编辑器中占用更多空间。如果你不想避免它们，那就把它们弄乱。

正确做法 👍🏻

```c
const char* fruits[] = {"apple",
"orange", "grape", "pineapple"};
    const char* toppings[] = {"syrup", "cream", 
                "jam", 
                "chocolate"};
char desserts[100][100];
int i = 0;
for (int f = 0; f < 4; f++) {
for (int t = 0; t < 4; t++) {
    sprintf(desserts[i], "%s with %s",
fruits[f],toppings[t]);
    i++;}}
```

错误做法 👎🏻

```c
const char* fruits[] = {"apple", "orange", "grape", "pineapple"};
const char* toppings[] = {"syrup", "cream", "jam", "chocolate"};
char desserts[100][100];
int i = 0;

for (int f = 0; f < 4; f++) {
    for (int t = 0; t < 4; t++) {
        sprintf(desserts[i], "%s with %s", fruits[f], toppings[t]);
        i++;
    }
}
```

### 💩 总是将你的逻辑判断的变量命名为 `flag`

布尔变量统一命名为 `flag` ,如果有多个逻辑变量，那就定义成 `flag+数字`，以此类推
至于这个逻辑变量到底是判断啥逻辑的，你别管，让你的协作者猜就好了

正确做法 👍🏻

```c
bool flag = 1;
```

错误做法 👎🏻

```c
bool isDone = 0;
bool isEmpty = 0;
```

### 💩 长函数比短函数更好

不要将程序逻辑分割成可读的片段。如果你的IDE搜索功能出故障，你将无法找到必要的文件或函数，那该怎么办？

- 10000 行代码在一个文件中是可以的。
- 1000 行的函数体是可以的。
- 在一个 `service.c` 中处理许多服务（第三方和内部的，还有一些辅助工具、手写的数据库ORM和套接字实现）？没问题。

### 💩 避免用测试覆盖你的代码

这是重复和不必要的工作量。代码能跑就行了，还测试啥

### 💩 尽可能避免使用代码检查工具

按照你想要的方式编写代码，尤其是当团队中有多个开发人员时。这是一种"自由"原则。

### 💩 在没有 README 文件的情况下开始你的项目

写啥说明文档啊，让用户自己摸索就好了

### 💩 代码冗余是有必要的

不要删除你的程序没有使用的代码。最多，注释掉它。
