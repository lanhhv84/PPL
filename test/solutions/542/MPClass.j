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

.method public static fib(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	goto Label1
	goto Label5
Label4:
Label5:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/fib(I)I
	iload_0
	iconst_2
	isub
	invokestatic MPClass/fib(I)I
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_5
	invokestatic MPClass/fib(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method
