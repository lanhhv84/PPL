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
.var 1 is s I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
	iconst_1
	istore_2
	bipush 7
	invokestatic MPClass/fact(I)I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static fact(I)I
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
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MPClass/fact(I)I
	imul
	goto Label1
Label5:
Label1:
	ireturn
.limit stack 6
.limit locals 1
.end method
