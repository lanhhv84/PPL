.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static x I

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

.method public static foo()Z
Label0:
	ldc "in foo "
	invokestatic io/putString(Ljava/lang/String;)V
	sipush 1000
	putstatic MPClass/x I
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	putstatic MPClass/x I
	getstatic MPClass/x I
	bipush 100
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	invokestatic MPClass/foo()Z
	ifle Label4
	goto Label5
Label4:
	iconst_0
	goto Label6
Label5:
	iconst_1
Label6:
	ifle Label7
	ldc "in then"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label8
Label7:
	ldc "in else"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label8:
Label1:
	return
.limit stack 5
.limit locals 1
.end method
