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

.method public static hello([Ljava/lang/String;)V
.var 0 is x [Ljava/lang/String; from Label0 to Label1
.var 1 is x_copy [Ljava/lang/String; from Label0 to Label1
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
	ldc "HELLO"
	aastore
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 31
.limit locals 3
.end method

.method public static goodbye([Ljava/lang/String;)V
.var 0 is x [Ljava/lang/String; from Label0 to Label1
.var 1 is x_copy [Ljava/lang/String; from Label0 to Label1
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
	ldc "GOODBYE"
	aastore
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 31
.limit locals 3
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
	ldc 5
	anewarray java/lang/String
	astore_1
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
	ldc "HI"
	aastore
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
	aload_1
	invokestatic MPClass/hello([Ljava/lang/String;)V
	aload_1
	invokestatic MPClass/printArray([Ljava/lang/String;)V
	aload_1
	invokestatic MPClass/goodbye([Ljava/lang/String;)V
	aload_1
	invokestatic MPClass/printArray([Ljava/lang/String;)V
Label1:
	return
.limit stack 11
.limit locals 3
.end method
