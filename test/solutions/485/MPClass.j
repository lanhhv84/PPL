.source MPClass.java
.class public MPClass
.super java.lang.Object


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
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is d F from Label0 to Label1
	iconst_0
	i2f
	fstore_1
	ldc 2
	newarray float
	astore 4
	iconst_2
	istore_2
	iconst_4
	istore_3
	aload 4
	iconst_1
	iload_2
	isub
	ineg
	iconst_0
	i2f
	fastore
	aload 4
	iconst_1
	iload_2
	isub
	ineg
	faload
	iload_3
	i2f
	fadd
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 14
.limit locals 5
.end method
