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
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
	iconst_1
	istore_1
	iload_1
	invokestatic io/putInt(I)V
	ldc 1.5
	fstore_3
	iconst_1
	istore 4
	fload_3
	iload 4
	i2f
	fadd
	ldc 0.15
	fadd
	invokestatic io/putFloat(F)V
	iconst_1
	istore 4
	iload 4
	istore_3
	iload_3
	invokestatic io/putBool(Z)V
	iload_1
	iconst_2
	iadd
	istore_1
	iconst_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 9
.limit locals 5
.end method
