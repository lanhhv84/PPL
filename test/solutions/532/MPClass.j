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
	ldc 5
	newarray int
	astore_1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
.var 4 is temp I from Label0 to Label1
	iconst_2
	i2f
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
.limit locals 5
.end method
