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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass/x I
Label4:
	getstatic MPClass/x I
	iconst_0
	if_icmpgt Label3
	goto Label2
Label2:
	getstatic MPClass/x I
	iconst_1
	iadd
	putstatic MPClass/x I
	goto Label4
Label3:
	getstatic MPClass/x I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method
