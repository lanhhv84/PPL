.source MPClass.java
.class public MPClass
.super java.lang.Object

.field static up I

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
.var 1 is a I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is b F from Label0 to Label1
	bipush 10
	putstatic MPClass/up I
	iconst_0
	istore_1
	getstatic MPClass/up I
	istore_2
Label8:
	iload_2
	iconst_1
	if_icmplt Label3
	iload_1
	bipush 40
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	goto Label2
	goto Label7
Label6:
Label7:
	iload_1
	iload_2
	iadd
	istore_1
Label2:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label8
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 8
.limit locals 4
.end method
