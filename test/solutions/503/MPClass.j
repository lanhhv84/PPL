.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static z I
.field static b [F

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	ldc 3
	newarray float
	putstatic MPClass/b [F
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is e I from Label0 to Label1
.var 2 is x F from Label0 to Label1
.var 3 is z Ljava/lang/String; from Label0 to Label1
	bipush 12
	istore_1
	bipush 12
	bipush 100
	imul
	i2f
	fstore_2
	getstatic MPClass/b [F
	iconst_0
	iconst_1
	isub
	ineg
	iload_1
	i2f
	fload_2
	fadd
	sipush 200
	i2f
	fsub
	fastore
	getstatic MPClass/b [F
	iconst_0
	iconst_1
	isub
	ineg
	faload
	invokestatic io/putFloatLn(F)V
	invokestatic MPClass/foo()V
Label1:
	return
.limit stack 9
.limit locals 4
.end method

.method public static foo()V
Label0:
	getstatic MPClass/b [F
	iconst_0
	iconst_1
	isub
	ineg
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 0
.end method
