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
.var 1 is x I from Label0 to Label1
.var 2 is y F from Label0 to Label1
.var 3 is z Z from Label0 to Label1
	bipush 23
	ineg
	bipush 34
	isub
	i2f
	invokestatic io/putFloatLn(F)V
	ldc 3232323.2323266566
	fneg
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method
