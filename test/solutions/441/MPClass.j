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
	iconst_1
	iconst_1
	isub
	ineg
	iconst_0
	iconst_1
	isub
	ineg
	iand
	invokestatic io/putBoolLn(Z)V
	bipush 12
	i2f
	iconst_5
	i2f
	fdiv
	bipush 9
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_1
	isub
	ineg
	iconst_4
	iconst_4
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 8
.limit locals 4
.end method
