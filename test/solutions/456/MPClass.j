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

.method public static foo()[Ljava/lang/String;
Label0:
	ldc 5
	anewarray java/lang/String
	astore_0
.var 1 is i I from Label0 to Label1
	iconst_2
	ineg
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpgt Label3
	aload_0
	iconst_2
	ineg
	iload_1
	isub
	ineg
	ldc "HELLO"
	aastore
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 11
.limit locals 2
.end method

.method public static printArray([Ljava/lang/String;)V
.var 0 is a [Ljava/lang/String; from Label0 to Label1
.var 1 is a_copy [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	astore_1
	aload_0
	aload_1
	iconst_2
	ineg
	bipush -2
	isub
	ineg
	aload_0
	iconst_2
	ineg
	bipush -2
	isub
	ineg
	aaload
	aastore
	aload_0
	aload_1
	iconst_2
	ineg
	iconst_m1
	isub
	ineg
	aload_0
	iconst_2
	ineg
	iconst_m1
	isub
	ineg
	aaload
	aastore
	aload_0
	aload_1
	iconst_2
	ineg
	iconst_0
	isub
	ineg
	aload_0
	iconst_2
	ineg
	iconst_0
	isub
	ineg
	aaload
	aastore
	aload_0
	aload_1
	iconst_2
	ineg
	iconst_1
	isub
	ineg
	aload_0
	iconst_2
	ineg
	iconst_1
	isub
	ineg
	aaload
	aastore
	aload_0
	aload_1
	iconst_2
	ineg
	iconst_2
	isub
	ineg
	aload_0
	iconst_2
	ineg
	iconst_2
	isub
	ineg
	aaload
	aastore
Label0:
.var 2 is i I from Label0 to Label1
	iconst_2
	ineg
	istore_2
Label4:
	iload_2
	iconst_2
	if_icmpgt Label3
	aload_1
	iconst_2
	ineg
	iload_2
	isub
	ineg
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 26
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/foo()[Ljava/lang/String;
	invokestatic MPClass/printArray([Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
