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
.var 1 is i I from Label0 to Label1
Label0:
	bipush 10
	istore_1
Label4:
	iload_1
	iconst_0
	if_icmplt Label3
	iload_1
	invokestatic io/putInt(I)V
Label2:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
