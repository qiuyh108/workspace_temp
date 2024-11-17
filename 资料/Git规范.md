---
title: Git规范
date: 2020-12-23 15:36:58
categories: Git
tags: 
todo:
---

# Git规范

## 提交描述规范

	feat: 添加新特性、新功能（feature）
	 
	fix: 修复bug
	 
	docs: 文档改变（documentation）
	 
	style: 代码格式改变，不改变代码逻辑（不影响代码运行的变动）
	 
	refactor: 代码重构，没有加新功能或者修复bug
	
	perf: 优化相关，比如提升性能、体验（performance profiling）
 
	test: 增加测试代码
	 
	chore: 改变构建流程、或者增加依赖库、关联包升级、工具等

	revert: 回滚到上一个版本

	//自定义,博客用
	add: 添加博客
	update: 更新原有博客


## 开发中git分支管理

	master/main: 主分支，只可合并，不可修改，保存每个上线版本完整代码

	release: 各个版本发布代码的版本，版本发布完成之后合并至master 

	develop: 开发专用,功能提测完成无误之后合并至release分支，并在release分支打包发布

	feat-xxx/vxxx: 功能或者版本开发分支,功能提测完成之后合并至develop

	fix: bug修复，从属于develop分支；保持和develop代码同步，修复完成后合并至develop
	

## Tag格式&版本命名
	
> 严格模式： v + 主版本号(MajorVersion).子版本号(MinorVersion).阶段版本号.日期版本号.类型版本号(TypeLabel)

> 常规模式： v + 主版本号.子版本号.阶段版本号
 

TypeLabel:

- devel: 开发版本后缀
- Alpha: 表示该软件刚刚具有雏形，有了基本功能，大多用于开发者之间交流，bug还比较多，尚待修改完善。
- Beta: 表示该软件消除了严重的错误，但还需要大量测试来进一步修改剩下的bug，这部分修改主要针对UI。
- Rc: 表示该软件基本不存在会导致错误的严重bug，与正式版接近。
- Release: 该版本表示一个正式版本，此版本会面向用户，称为标准版。简写为R。
