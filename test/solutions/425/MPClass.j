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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	ldc 4
	newarray int
	astore_1
.var 2 is ind I from Label0 to Label1
Label0:
	bipush 101
	istore_2
	aload_1
	bipush 99
	iload_2
	isub
	ineg
	bipush 69
	iastore
	aload_1
	iload_2
	invokestatic MPClass/main2([II)V
Label1:
	return
.limit stack 14
.limit locals 3
.end method

.method public static main2([II)V
.var 1 is a I from Label0 to Label1
Label0:
	aload_0
	bipush 99
	iload_1
	isub
	ineg
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 2
.end method