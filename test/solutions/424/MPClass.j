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
	bipush 60
	invokestatic MPClass/main2(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main2(I)V
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
