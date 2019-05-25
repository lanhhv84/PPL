import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_redeclared_global_1(self):
        inp = """
        var main: real;
        procedure main();
        begin
        end
        """
        exp = str(Redeclared('Procedure', 'main'))
        self.assertTrue(TestChecker.test(inp, exp, 401))

    def test_redeclared_global_2(self):
        inp = """
        var a69: real;
        var a96: real;
        var a69: string;
        procedure main();
        begin
        end
        """
        exp = str(Redeclared('Variable', 'a69'))
        self.assertTrue(TestChecker.test(inp, exp, 402))

    def test_redeclared_global_3(self):
        inp = """
        var a69, a69: real;
        procedure main();
        begin
        end
        """
        exp = str(Redeclared('Variable', 'a69'))
        self.assertTrue(TestChecker.test(inp, exp, 403))

    def test_redeclared_global_4(self):
        inp = """
        var a69: real;
        procedure main();
        begin

        end
        var a69: string;
        """
        exp = str(Redeclared('Variable', 'a69'))
        self.assertTrue(TestChecker.test(inp, exp, 404))

    def test_redeclared_global_5(self):
        inp = """
        var a69: real;
        procedure main();
        begin

        end

        function main(): integer;
        begin
            return 1;
        end
        """
        exp = str(Redeclared('Function', 'main'))
        self.assertTrue(TestChecker.test(inp, exp, 405))

    def test_redeclared_global_6(self):
        inp = """
        var a69: real;
        procedure main();
        begin

        end

        procedure main();
        begin

        end
        """
        exp = str(Redeclared('Procedure', 'main'))
        self.assertTrue(TestChecker.test(inp, exp, 406))

    def test_redeclared_global_7(self):
        inp = """
        function main(): integer;
        begin
            return 1;
        end

        procedure main();
        begin
            return;
        end

        
        """

        exp = str(Redeclared('Procedure', 'main'))
        self.assertTrue(TestChecker.test(inp, exp, 407))


    def test_redeclared_local_8(self):
        inp = """
        procedure main();
        begin end
        procedure func(a: integer; a: real);
        begin
        end

        

        
        """

        exp = str(Redeclared('Parameter', 'a'))
        self.assertTrue(TestChecker.test(inp, exp, 408))

    def test_redeclared_local_9(self):
        inp = """
        procedure func(a: integer; c: real; a: real);
        begin
        end
        
        procedure main();
        begin end

        

        procedure mainerror();
        begin end

        """
        exp = str(Redeclared('Parameter', 'a'))
        self.assertTrue(TestChecker.test(inp, exp, 409))

    def test_redeclared_local_10(self):
        inp = """

        procedure func(a: integer);
        var b, c, d, a: real;
        begin
        end

        procedure main();
        begin end

        
        """
        exp = str(Redeclared(Variable(), 'a'))
        self.assertTrue(TestChecker.test(inp, exp, 410))


    def test_redeclared_block_11(self):
        inp = """
        procedure main();
        begin
        with a,b:integer;
            do
            begin
                a := a + 10 -9 div b mod b - b * b div 1 mod 1 - 1 * 1;
                break;
            end
        end
        """

        exp = str(BreakNotInLoop())
        self.assertTrue(TestChecker.test(inp, exp, 411))

    def test_redeclared_block_12(self):
        inp = """
        function c(): real;
        begin
        with a,b:integer;c:array [69 .. 96] of real;
            do 
            begin
            a := a + 10;
            continue;
            return -1.0;
            end
        end
        
        procedure main();
        begin end

        
        """
        exp = str(ContinueNotInLoop())
        self.assertTrue(TestChecker.test(inp, exp, 412))

    def test_undeclared_var_13(self):
        inp = """
        procedure main();
        begin
        xyz(a);
        end

        procedure xyz(abc: integer);
        begin
        end
        """
        exp = str(Undeclared(Identifier(), 'a'))
        self.assertTrue(TestChecker.test(inp, exp, 413))

    def test_notreturn(self):
        input = """
                Function aaaa(N:array[1 .. 2] of integer) :Integer;
                Var i:Integer;
                Begin
                 For i:= N[i] to 0 do
                  If(N[i] mod i = 0) then
                    return 1;
                  Else
                    return 2;
                End

                procedure main();
                begin
                end
                """
        expect = str(FunctionNotReturn('aaaa'))
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_duplicate(self):
        inp = """
        procedure main ();
            var a, b, c: real;
                a: array [1 .. 69] of integer;
         begin
        end
        """

        expect = str(Redeclared(Variable(), 'a'))
        self.assertTrue(TestChecker.test(inp,expect,415))

    def test_duplicate_2(self):
        inp = """
            function main(a, b: real; b: array [69 .. 96] of string): real;
            begin
            return;
            end
        """
        expect = str(Redeclared(Parameter(), 'b'))
        self.assertTrue(TestChecker.test(inp,expect,416))    

    def test_duplicate_3(self):
        inp = """
            function main(a, b: real): real;
            var c, d, a: array [69 .. 98] of string;
            begin 
            end
        """
        expect = str(Redeclared(Variable(), 'a'))
        self.assertTrue(TestChecker.test(inp,expect,417))  

    def test_callexpr_1(self):
        inp = """
            procedure main();
            begin
            end


            function test(a, b: integer): real;
            begin
                return 999;
            end

            function main2(a, c: real): real;
            begin
                return test(a, c);
            end
        """

        expect = str(TypeMismatchInExpression(CallExpr(Id('test'), [Id('a'), Id('c')])))
        self.assertTrue(TestChecker.test(inp,expect,418))  

    def test_callexpr_2(self):
        inp = """
            function test(a, b: real): integer;
            begin
                return test(1, 1.1);
            end

            function test2(a: real): integer;
            begin
                return (98);
            end

            function main(a, c: integer): real;
            begin
                a := test(a, c);
                a := test2(a,1);
            end
        """

        expect = str(TypeMismatchInExpression(CallExpr(Id('test2'), [Id('a'), IntLiteral(1)])))
        self.assertTrue(TestChecker.test(inp,expect,419))

    def test_for_1(self):
        inp = """
        function main(a, b: real; c: integer): real;
        begin
            for a := c downto c do
                begin
                end
        end
        """
        exp = str(TypeMismatchInStatement(For(Id('a'), Id('c'), Id('c'), False, [])))
        self.assertTrue(TestChecker.test(inp,exp,420)) 

    def test_for_2(self):
        inp = """
        function main(a, b: real; c: integer): real;
        begin
            for c := 1 downto 2 do
                begin
                end

            for c := 1.0 downto 2 do
                begin
                end
        end
        """
        exp = str(TypeMismatchInStatement(For(Id('c'), FloatLiteral(1.0), IntLiteral(2), False, [])))
        self.assertTrue(TestChecker.test(inp,exp,421)) 

    def test_for_3(self):
        inp = """
        function main(a, b: real; c: integer): real;
        begin
            for c := 1 downto c do
                begin
                end

            for c := 1 to 2 do
                begin
                end

            for c := b to 2 do
                begin
                end
        end
        """
        exp = str(TypeMismatchInStatement(For(Id('c'), Id('b'), IntLiteral(2), True, [])))
        self.assertTrue(TestChecker.test(inp,exp,422)) 

    def test_op_1(self):
        inp = """
        function main(a, b: real; c: integer): real;
        begin
            for c := 1 downto c do
                begin
                    c := 1 + 1.2;
                end

        end
        """
        exp = str(TypeMismatchInStatement(Assign(Id('c'), BinaryOp('+', IntLiteral(1), FloatLiteral(1.2)))))
        self.assertTrue(TestChecker.test(inp,exp,423)) 

    def test_op_2(self):
        inp = """
        function main(a, b: real; c: integer): real;
        begin
            b := 1 * 9;
            c := c * b;
        end
        """
        exp = str(TypeMismatchInStatement(Assign(Id('c'), BinaryOp('*', Id('c'), Id('b')))))
        self.assertTrue(TestChecker.test(inp,exp,424)) 

    def test_op_4(self):
        inp = """
        function main(a, b: real; c: integer): real;
        begin
            b := 1 * 9;
            for c := 9*1+2 to 69+96*96*56 do
                for c := 69 downto 96+9+9+9+9 do
                    for c := 1254 downto 45 + 32 do
                        c := 9 / 9;
        end
        """
        exp = str(TypeMismatchInStatement(Assign(Id('c'), BinaryOp('/', IntLiteral(9), IntLiteral(9)))))
        self.assertTrue(TestChecker.test(inp,exp,425)) 

    def test_op_5(self):
        inp = """
        var a: integer;
        """
        exp = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(inp,exp,426)) 

    def test_all(self):
        inp = """
        var a: integer;
            var b: string;
            var c: real;
            var d: boolean;
            procedure main();                
            begin
                a:=foo3();
            end

            function foo3(): integer;
            var i:integer;
            begin
                if(d) then
                    return foo1();
                for i:= foo1() to - e[foo1()] do begin
                        return e[-foo1()];
                    end
                return 1;
            end


            function foo(): integer;
            var i:integer;
            begin
                return e[foo1()];
            end

            function foo1(): integer;
            var i:integer;
            begin
                return 1;
            end
            
            var e: array[1 .. 3] of integer;
        """

        exp = str(Unreachable(Function(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,427)) 


    def test_428(self):
        inp = """
        var x, y, z: integer;
        var arr: array [10 .. 90] of integer;
        
        procedure main();
        begin
            while x + y > z do
                while x + 9 <= arr[2933] do
                    while ((x + 9 > 3 + 2 or else 86 + foo() * foo() = 3) and then (fii() + fii () > (fii() - fii()))) do
                        while fii() > fii() or else foo() <= fii() do
                            begin
                                foo() := 99;
                            end
        end


        function foo(): integer;
        begin
            return foo();
        end

        function fii(): integer;
        begin
            return fii();
        end
        """
        exp = str(TypeMismatchInStatement(Assign(CallExpr(Id('foo'), []), IntLiteral(99))))
        self.assertTrue(TestChecker.test(inp,exp,428)) 

    def test_1_429(self):
        inp = """
        var def: integer;
        procedure main();
        begin
        end

        function DeF():integer;
        begin
            return 9346384 + 294718 -246284 mod 36573563;
        end
        """

        exp = str(Redeclared(Function(), 'DeF'))
        self.assertTrue(TestChecker.test(inp,exp,429)) 

    def test_1_430(self):
        inp = """
        var b: integer;
                    procedure main();
                    begin
                        putIntLn(a);
                    end
                    function a():real;
                    begin
                    end
        """
        exp = str(Undeclared(Identifier(), 'a'))
        self.assertTrue(TestChecker.test(inp,exp,430)) 
    
    def test_undeclared_parameter_431(self):
        inp = """
        var a, k98, j78: integer;
        var J: array [-98 .. -100] of string;
        procedure main();
        begin
            a := foo2(kj);
            foo(J);
        end

        procedure foo(a: array [-98 .. -100] of string);
        begin
        end
        function foo2(a: array [-98 .. -100] of string): integer;
        begin
            return 1228948124121490701750730105;
        end
        """

        exp = str(Undeclared(Identifier(), 'kj'))
        self.assertTrue(TestChecker.test(inp,exp,431))

    def test_undeclared_parameter_432(self):
        inp = """
        var a, k98, j78: integer;
        var J: array [-98 .. -100] of string;
        procedure main();
        begin
            a := foo2(kj);
        end

        procedure foo(a: array [-98 .. -100] of string);
        begin
        end

        function foo2(a: array [-98 .. -100] of string): integer;
        begin
            return 1228948124121490701750730105;
        end
        """

        exp = str(Undeclared(Identifier(), 'kj'))
        self.assertTrue(TestChecker.test(inp,exp,432))

    def test_undeclared_function_433(self):
        inp = """
            var jhkf: array [-100 .. 8512795125] of string;

            procedure main();
            begin 
                jhkf := foo();
            end

            procedure foo();
            begin
            end
        """
        exp = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,433))

    def test_undeclared_function_434(self):
        inp = """
            var jhkf: array [-100 .. 8512795125] of string;
            procedure main();
            begin 
                jhkf := foo();
            end
        """
        exp = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,434))

    def test_undeclared_function_435(self):
        inp = """
            var jhkf: array [-100 .. 8512795125] of string;
            var foo: integer;
            procedure main();
            begin 
                jhkf := foo();
            end
        """
        exp = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,435))

    def test_undeclared_procedure_436(self):
        inp = """
            var jhkf: array [-100 .. 8512795125] of string;
            var foo: integer;
            procedure main();
            begin 
                foo();
            end
        """
        exp = str(Undeclared(Procedure(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,436))

    def test_undeclared_procedure_437(self):
        inp = """
            var jhkf: array [-100 .. 8512795125] of string;
            procedure main();
            begin 
                foo();
            end
        """
        exp = str(Undeclared(Procedure(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,437))

    def test_undeclared_procedure_438(self):
        inp = """
            var jhkf: array [-100 .. 8512795125] of string;
            procedure main();
            begin 
                foo();
            end

            function foo(): real;
            begin
                return 1/1;
            end
        """
        exp = str(Undeclared(Procedure(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,438))

    def test_undeclared_variable_439(self):
        inp = """
            var jhkf: array [-100 .. 8512795125] of string;
            procedure main();
            begin 
                hdhfid := foo();
            end

            function foo(): real;
            begin
                return 1/1;
            end
        """
        exp = str(Undeclared(Identifier(), 'hdhfid'))
        self.assertTrue(TestChecker.test(inp,exp,438))

    def test_undeclared_identifier_439(self):
        inp = """
            var jhkf: array [-100 .. 8512795125] of string;
            procedure main();
            begin 
                jhkf := 8924 + foo /4 + 9 mod 85;
            end
        """
        exp = str(Undeclared(Identifier(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,439))

    def test_undeclared_identifier_440(self):
        inp = """
            var jhkf: InteGer;
            var FOO: integer;
            var BaR: integer;
            procedure main();
            begin 
                jHkF := 8924 + fOo * 4 + 9 mod 85 - bAr;
                return 12;
            end
        """
        exp = str(TypeMismatchInStatement(Return(IntLiteral(12))))
        self.assertTrue(TestChecker.test(inp,exp,440))

    def test_typemm_stmt_441(self):
        inp = """
        var abc: integer;
            procedure main();
            begin
                if (1 + 2) then
                    if true then
                        iF faLse then
                            pUtInTlN(12312); 
            end
        """
        exp = str(TypeMismatchInStatement(If(BinaryOp('+',IntLiteral(1), IntLiteral(2)), [If(BooleanLiteral(True), [If(BooleanLiteral(False), [CallStmt(Id('pUtInTlN'), [IntLiteral(12312)])])])])))
        self.assertTrue(TestChecker.test(inp,exp,441))

    def test_typemm_stmt_442(self):
        inp = """
            var i: integer;
            procedure main();
            begin
                for i := 1.1 downto 99 do
                    fOO();
            end

            procedure foo();
            begin end
        """
        exp = str(TypeMismatchInStatement(For(Id('i'), FloatLiteral(1.1), IntLiteral(99), False, [CallStmt(Id('fOO'), [])])))
        self.assertTrue(TestChecker.test(inp,exp,442))

    def test_typemm_stmt_443(self):
        inp = """
            var i: real;
            procedure main();
            begin
                for i := 99 downto 99 do
                    fOO();
            end

            procedure foo();
            begin end
        """
        exp = str(TypeMismatchInStatement(For(Id('i'), IntLiteral(99), IntLiteral(99), False, [CallStmt(Id('fOO'), [])])))
        self.assertTrue(TestChecker.test(inp,exp,443))

    def test_typemm_stmt_444(self):
        inp = """
            procedure main();
            begin
                with i: integer; j: real; do
                    for i := 99 downto j do
                        fOO();
            end

            procedure foo();
            begin end
        """
        exp = str(TypeMismatchInStatement(For(Id('i'), IntLiteral(99), Id('j'), False, [CallStmt(Id('fOO'), [])])))
        self.assertTrue(TestChecker.test(inp,exp,444))

    def test_typemm_stmt_445(self):
        inp = """
            procedure main();
            begin
                while (1 + 2) do
                    with i: integer; j: integer; do
                        for i := 99 downto j do
                            fOO();
            end

            procedure foo();
            begin end
        """
        exp = str(TypeMismatchInStatement(While(BinaryOp('+', IntLiteral(1), IntLiteral(2)), [With([VarDecl(Id('i'), IntType()), VarDecl(Id('j'), IntType())], [For(Id('i'), IntLiteral(99), Id('j'), False, [CallStmt(Id('fOO'), [])])])])))
        self.assertTrue(TestChecker.test(inp,exp,445))

    def test_typemm_stmt_446(self):
        inp = """
        procedure main();
        var a, b: string;
        begin
            a := b;
        end
        """
        exp = str(TypeMismatchInStatement(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(inp,exp,446))

    def test_typemm_stmt_447(self):
        inp = """
        procedure main();
        var a, b: array [100 .. 1] of string;
        begin
            a := b;
        end
        """
        exp = str(TypeMismatchInStatement(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(inp,exp,447))

    def test_typemm_stmt_448(self):
        inp = """
        procedure main();
        var a, b: array [100 .. 1] of string;
        begin
            a := b;
        end
        """
        exp = str(TypeMismatchInStatement(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(inp,exp,448))

    def test_typemm_stmt_448(self):
        inp = """
        procedure main();
        var ahihi, b: integer;
            a, c: real;
            d: boolean;
            g : boolean;
        begin
            a := c;
            a := b + c / c + c - c / c;
            d := ((b <= c) or (b >= c)) or else ((b = c) and then ((b < c) and (b > c)));
            g := d;
            d := g;
            ahihi := c;
        end
        """
        exp = str(TypeMismatchInStatement(Assign(Id('ahihi'), Id('c'))))
        self.assertTrue(TestChecker.test(inp,exp,448))

    def test_typemm_stmt_449(self):
        inp = """
        procedure main();
        var ahihi, b: integer;
            c: real;
            d: boolean;
            g : boolean;
        begin
            return b <= c or b >= c;
        end
        """
        exp = str(TypeMismatchInStatement(Return(BinaryOp('>=',BinaryOp('<=',Id('b'),BinaryOp('or',Id('c'),Id('b'))),Id('c')))))
        self.assertTrue(TestChecker.test(inp,exp,449))

    def test_typemm_stmt_450(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := foo();
         end

        function foo():integer;
        begin
            return;
        end
        """

        exp = str(TypeMismatchInStatement(Return()))
        self.assertTrue(TestChecker.test(inp,exp,450))

    def test_typemm_expr_451(self):
        inp = """
        procedure main();
        var a: string;
            arr: array [199 .. 99] of string;
        begin 
            foo(arr[100]);
            foo(a);
            return a;
        end

        procedure foo(a: string);
        begin
        end
        """

        exp = str(TypeMismatchInStatement(Return(Id('a'))))
        self.assertTrue(TestChecker.test(inp,exp,451))

    def test_typemm_expr_452(self):
        inp = """
        procedure main();
        var a: string;
            arr: array [199 .. 99] of string;
        begin 
            foo(arr[-100]);
            foo(a);
            return a;
        end

        procedure foo(a: string);
        begin
        end
        """

        exp = str(TypeMismatchInStatement(Return(Id('a'))))
        self.assertTrue(TestChecker.test(inp,exp,452))

    def test_typemm_expr_453(self):
        inp = """
        procedure main();
        var a: string;
            arr: array [199 .. 99] of string;
        begin 
            foo(arr[-1.1]);
            foo(a);
            return a;
        end

        procedure foo(a: string);
        begin
        end
        """

        exp = str(TypeMismatchInExpression(ArrayCell(Id('arr'), UnaryOp('-', FloatLiteral(1.1)))))
        self.assertTrue(TestChecker.test(inp,exp,453))

    def test_function_return_454(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := foo();
        end

        function foo(): integer;
        begin
        end
        """
        exp = str(FunctionNotReturn('foo'))
        self.assertTrue(TestChecker.test(inp,exp,454))
        

    def test_function_return_455(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a := foo();
        end

        function foo(): integer;
        begin
            return 98 >= 99;
        end
        """
        exp = str(TypeMismatchInStatement(Return(BinaryOp('>=', IntLiteral(98), IntLiteral(99)))))
        self.assertTrue(TestChecker.test(inp,exp,455))

    def test_break_continue_456(self):
        inp = """
            procedure main();
            var i: integer;
            begin

                for i := 1 to 10 do
                begin
                    with x: real; do
                    begin
                        break;
                    end
                end
            end
        """

        exp = str([True])
        self.assertTrue(TestChecker.test(inp,exp,456))

    def test_break_continue_457(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            for i := 1 to 10 do
            begin
                if True then break; else break;
            end
            return 99;
        end
        """
        exp = str(TypeMismatchInStatement(Return(IntLiteral(99))))
        self.assertTrue(TestChecker.test(inp,exp,457))

    def test_break_continue_458(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            for i := 1 to 10 do
            begin
                if True then break; else break;
            end
            return 99;
        end
        """
        exp = str(TypeMismatchInStatement(Return(IntLiteral(99))))
        self.assertTrue(TestChecker.test(inp,exp,458))

    def test_break_continue_459(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            for i := 1 to 10 do
            begin
                if True then break; else break;
            end
            break;


        end
        """
        exp = str(BreakNotInLoop())
        self.assertTrue(TestChecker.test(inp,exp,459))

    def test_break_continue_460(self):
        inp = """
        procedure main();
        var i: integer;
        begin
            while i <= 99 do
            begin
                break;
            end
            continue;
        end
        """
        exp = str(ContinueNotInLoop())
        self.assertTrue(TestChecker.test(inp,exp,460))

    def test_entry_point_461(self):
        inp = """
        procedure main2();
        begin

        end
        """
        exp = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(inp,exp,461))

    def test_unreachable_stmt_462(self):
        inp = """
        procedure main();
        var i, a: integer;
        begin
            for i := a downto a do
                begin
                    if a >= 10 then
                        break;
                    else
                        break;
                    break;
                end
        end
        """
        exp = str(UnreachableStatement(Break()))
        self.assertTrue(TestChecker.test(inp,exp,462))

    def test_unreachable_stmt_463(self):
        inp = """
        procedure main();
        begin
            while ((99 <= 98) or else(78 >= 87)) do
                begin
                    break;
                    foo();
                end
        end

        procedure foo();
        begin 
        end
        """

        exp = str(UnreachableStatement(CallStmt(Id('foo'), [])))
        self.assertTrue(TestChecker.test(inp,exp,463))

    def test_unreachable_stmt_464(self):
        inp = """
        procedure main();
        begin
            while ((99 <= 98) or else(78 >= 87)) do
                begin
                    continue;
                    foo();
                end
        end

        procedure foo();
        begin 
        end
        """

        exp = str(UnreachableStatement(CallStmt(Id('foo'), [])))
        self.assertTrue(TestChecker.test(inp,exp,464))

    def test_unreachable_stmt_465(self):
        inp = """
        procedure main();
        begin
            while ((99 <= 98) or else(78 >= 87)) do
                begin
                    continue;
                    foo();
                end
        end

        procedure foo();
        begin 
        end
        """

        exp = str(UnreachableStatement(CallStmt(Id('foo'), [])))
        self.assertTrue(TestChecker.test(inp,exp,465))

    def test_unreachable_func_466(self):
        inp = """
        procedure main();
        var a: real;
        begin
            while ((99 <= 98) or else(78 >= 87)) do
                begin
                    a := getFloat();
                end
        end

        procedure foo();
        begin 
        end
        """
        exp = str(Unreachable(Procedure(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,466))

    def test_unreachable_func_467(self):
        inp = """
        procedure main();
        var a: real;
        begin
            while ((99 <= 98) or else(78 >= 87)) do
                begin
                    a := getInt();
                end
        end

        procedure foo();
        begin 
        end
        """
        exp = str(Unreachable(Procedure(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,467))

    def test_redeclared_var_468(self):
        inp = """
        var foo, bar, tees: integer;
        procedure main();
        var foo, bar, tees: real;
        begin
            return;
        end

        function ffoo(): real;
        begin
            return foo + bar + tees;
        end
        """
        exp = str(Unreachable(Function(), 'ffoo'))
        self.assertTrue(TestChecker.test(inp,exp,468))

    def test_redeclared_var_469(self):
        inp = """
        var foo, bar, tees: integer;
        procedure main(foo: array [98 .. 99] of real);
        var foo, bar, tees: real;
        begin
            return;
        end

        function ffoo(): real;
        begin
            return foo + bar + tees;
        end
        """
        exp = str(Redeclared(Variable(), 'foo'))
        self.assertTrue(TestChecker.test(inp,exp,469))

    def test_redeclared_var_470(self):
        inp = """
        var foo, bar, tees: integer;
        procedure main();
        var foo, bar, tees: real;
        begin
            with foo, bar, tees: integer; foo_real: real; do
                begin
                    for foo := bar downto tees do
                        begin
                        foo := getInt();
                        foo := ffoo();
                        end
                end
            return;
        end

        function ffoo(): real;
        begin
            return foo + bar + tees;
        end
        """
        exp = str(TypeMismatchInStatement(Assign(Id('foo'), CallExpr(Id('ffoo'), []))))
        self.assertTrue(TestChecker.test(inp,exp,470))

    def test_redeclared_var_471(self):
        inp = """
        procedure main();
        begin
        end

        procedure getInt();
        begin
        end
        """
        exp = str(Redeclared(Procedure(), 'getInt'))
        self.assertTrue(TestChecker.test(inp,exp,471))
    
    def test_all_472(self):
        inp = '''
                procedure main();
                var i:integer;
                begin
                    i := 0;
                    while i < 100 do
                    begin
                        putIntLn(i);
                        i := i + 1;
                        if i = 60 then
                            return;
                        putStringLn("Hello Haskell!");
                        if i = 70 then
                            break;
                        else
                            continue;
                        putStringLn("Hello Smalltalk!");
                    end 
                end
            '''
        exp = "Unreachable statement: CallStmt(Id(putStringLn),[StringLiteral(Hello Smalltalk!)])"
        self.assertTrue(TestChecker.test(inp,exp,472))

    def test_all_473(self):
        inp = '''
        procedure main();
        var i:integer;
        begin
            i := getInt;
        end
            '''
        exp = str(Undeclared(Identifier(), 'getInt'))
        self.assertTrue(TestChecker.test(inp,exp,473))

    def test_all_474(self):
        inp = '''
        procedure main();
        var i:integer;
        begin
            i := putInt;
        end
            '''
        exp = str(Undeclared(Identifier(), 'putInt'))
        self.assertTrue(TestChecker.test(inp,exp,474))

    def test_all_475(self):
        inp = '''
        procedure main();
        var i:integer;
        begin
            i := putInt;
        end
            '''
        exp = str(Undeclared(Identifier(), 'putInt'))
        self.assertTrue(TestChecker.test(inp,exp,475))

    def test_all_476(self):
        inp = '''
            procedure main();
            begin
                foo(11111999, 16111998);
            end
            procedure foo(p, p:integer);
            begin
            end
        '''
        exp = str(Redeclared(Parameter(), 'p'))
        self.assertTrue(TestChecker.test(inp,exp,476))

    def test_all_477(self):
        inp = '''
            var i,j,k:integer;
            procedure main();
            begin
                for i := j + k to (k / h / j / j) div i do
                begin
                    putStringLn("I love Oanh Trinh");
                end
            end
        '''
        exp = str(Undeclared(Identifier(), 'h'))
        self.assertTrue(TestChecker.test(inp,exp,477))

    def test_all_478(self):
        inp = '''
            procedure main();
            begin
                HCMUT(getINT(), GETint(), gETInt());
                HCMUT(getint(), GETINT(), gEtInT());
            end
            procedure HCMUT(a,b,c:integer);
            begin
                for a := b + c downTO b <= c do
                begin
                    break;
                end
                return;
            end
        '''
        exp = str(TypeMismatchInStatement(For(Id('a'), BinaryOp('+', Id('b'),Id('c')),BinaryOp('<=',Id('b'),Id('c')),False,[Break()]))) 
        self.assertTrue(TestChecker.test(inp,exp,478))

    def test_all_479(self):
        input = '''
            var t: array[1 .. 2] of integer;
            procedure main();
            var foo: real;
            begin
                foo := func(t);
            end
            function Func(ab: array[1 .. 2] of integer):integer;
            var t: integer;
            begin
                ab[ab[10]] := t := 10;
                return ab[ab[t]] > ab[t];
            end
        '''
        expect = str(TypeMismatchInStatement(Return(BinaryOp('>',ArrayCell(Id('ab'),ArrayCell(Id('ab'),Id('t'))),ArrayCell(Id('ab'),Id('t'))))))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_all_480(self):
        input = '''
            function sum(x:array [0 .. 10] of real):real;
            var i:integer;
                S:real;
            begin
                S := 0;
                for i := 0 to 10 do
                    S := S + x[i];
                return S;
            end
            procedure main();
            var y:array[-0 .. 10] of real;
                z:array[-1 .. 9] of real;
            begin
                if sum(y) > 0 then
                    return;
                if sum(z) then
                    return;
            end
        '''
        expect = str(TypeMismatchInExpression(CallExpr(Id('sum'), [Id('z')])))
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_all_481(self):
        input = '''
            function FOO1():integer;
            begin
                with a,b:real;c:integer; do
                begin
                    while a + c > b do
                    begin
                        putStringLn("Hello C!");
                        return 0;
                    end
                    putStringLn("Hello C#!");
                    if a = b then
                    begin
                        putStringLn("Hello Ada!");
                        return 0;
                    end
                    else
                        return 0;
                end
            end
            function FOO():integer;
            var x, y: integer;
            begin
                if (x MOD y) = 2 then
                begin
                    putStringLn("Hello PHP!");
                    return 1;
                end
                else
                    putStringLn("Hello HTML!");
            end
            procedure main();
            var otr: integer;
            begin
                otr := foo();
                otr := foo1();
            end
        '''
        expect = str(FunctionNotReturn('FOO'))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_all_482(self):
        input = '''
            function foo():integer;
            begin
                return 0;
            end
            procedure main();
            begin
            end
        '''
        expect = str(Unreachable(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_all_483(self):
        input = """
            procedure main();
            var a: integer;
            begin
                a:= 1 or "abc";
            end
        """
        expect = str(TypeMismatchInExpression(BinaryOp('or', IntLiteral(1), StringLiteral('abc')))) 
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_all_484(self):
        inp = """
            procedure main();
            var a: integer;
            begin
                a:= 1 or else true;
            end
        """
        exp = str(TypeMismatchInExpression(BinaryOp('orelse', IntLiteral(1), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(inp,exp,484))

    def test_all_485(self):
        input = """
            procedure main();
            var a: integer;
            begin
                a:= 1 > false;
            end
            """
        expect = str(TypeMismatchInExpression(BinaryOp('>', IntLiteral(1), BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_all_486(self):
        inp = """
            procedure main();
            var a: integer;
            begin
                a:= 1.0 or 1.0;
            end
        """
        exp = str(TypeMismatchInExpression(BinaryOp('or', FloatLiteral(1.0), FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(inp,exp,486))

    def test_all_487(self):
        inp = """
            procedure main();
            var a: integer;
            begin
                a:= 1.0 div false;
            end
        """
        exp = str(TypeMismatchInExpression(BinaryOp('div', FloatLiteral(1.0), BooleanLiteral(False)))) 
        self.assertTrue(TestChecker.test(inp,exp,487))

    def test_all_488(self):
        inp = """
            procedure main();
            var a: integer;
            begin
                a:= "abc" <= true;
            end
            """
        exp = str(TypeMismatchInExpression(BinaryOp('<=', StringLiteral('abc'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(inp,exp,210))
    
    def test_all_489(self):
        inp = """
        procedure main();
        var a: integer;
        begin
            a:= "abc" > true;
        end
         """
        exp = str(TypeMismatchInExpression(BinaryOp('>', StringLiteral('abc'), BooleanLiteral(True)))) 
        self.assertTrue(TestChecker.test(inp,exp,489))

    def test_all_490(self):
        inp = """
            procedure main();
            var a: integer;
            begin
                a:= true / "abc";
            end
            """
        exp = str(TypeMismatchInExpression(BinaryOp('/', BooleanLiteral(True), StringLiteral('abc'))))  
        self.assertTrue(TestChecker.test(inp,exp,490))

    def test_all_491(self):
        inp = """
            procedure foo();
            var a:integer;
            begin
                while trUE do
                    continue;
                
                for a:=a doWNtO 0 do
                    continue;
            end

            procedure MaIn();
            begin
                foo();
                continue;  // error
            end
            """
        exp = str(ContinueNotInLoop())
        self.assertTrue(TestChecker.test(inp,exp,491))

    def test_all_492(self):
        input = """
            procedure main();
            var a: integer;
            begin
                a:= false < true;
                end
        """
        expect = str(TypeMismatchInExpression(BinaryOp('<', BooleanLiteral(False), BooleanLiteral(True)))) 
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_all_493(self):
        inp = """
            procedure main();
            var a: string;
            begin
                a:= 1 div 1.0;
            end
            """
        exp = str(TypeMismatchInExpression(BinaryOp('div', IntLiteral(1), FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(inp,exp,493))

    def test_all_494(self):
        inp = """
        procedure MaIn();
        var b: boolean;
            a: integer;
        begin
            a:=-a;
            b:=b;
            b:=-b;  // error
        end
        """
        exp = str(TypeMismatchInExpression(UnaryOp('-', Id('b'))))
        self.assertTrue(TestChecker.test(inp,exp,494))

    def test_all_495(self):
        """test_unreachable_stmt5"""
        inp = """
        procedure MaIn();
        var a:boolean;
        begin
            foo();
            foo5();
        end
                
        procedure foo();
        var a:integer;
        begin
            if True then
                begin
                    a:=a;
                    putintln(a);
                    return ;
                end
            else  //# no return
                begin
                    a:=0;
                    putintln(69);
                end
            a:=0;
        end

        procedure foo5();
        var a:integer;
        begin
            if True then
                begin
                    a:=a;
                    putintln(a);
                    return ;  //# return here
                end
            else
                begin
                    a:=0;
                    putintln(69);
                    return ;  //# return here
                end
            A:=0;  // error
        end
        """
        exp = str(UnreachableStatement(Assign(Id('A'), IntLiteral(0))))
        self.assertTrue(TestChecker.test(inp,exp,495))

    def test_all_496(self):
        """test_unreachable_stmt10"""
        inp = """
        procedure MaIn();
        begin
            foo();
            foo10();
        end

        procedure foo();  // error
        var a:integer;
        begin
            if True then  //# no return
                begin
                    a:=a;
                    putintln(a);
                    while True do
                        return;

                    for a:=0 downto a do
                        begin
                            return;
                        end
                end
            else
                begin
                    a:=0;
                    putintln(69);
                    return;
                end

            main();
        end

        procedure foo10();
        var a:integer;
        begin
            if True then
                begin
                    a:=a;
                    putintln(a);
                    while True do
                        break;
                        
                    return;  //# return here
                end
            else
                begin
                    a:=0;
                    putintln(69);
                    return;  //# return here
                end
                
            MAIN();  // error
        end
        """
        exp = str(UnreachableStatement(CallStmt(Id('MAIN'), []))) 
        self.assertTrue(TestChecker.test(inp,exp,496))

    def test_all_497(self):
        inp = """
    procedure MaIn();
    begin
        foo();
        foo16();
    end

    procedure foo();
    var a:integer;
    begin
        for a:=a to a do  //# no return
            begin
                with
                    b,c,d:real;
                do
                    begin
                        if b=c+d/a then
                            begin
                                if true and False then
                                    break;
                                else
                                    continue;
                            end
                        else
                            putfloatLN(1.3);
                    end
            end

        a := 1;
    end

    procedure foo16();
    var a:integer;
    begin
        for a:=a to a do
            begin
                with
                    b,c,d:real;
                do
                    begin
                        if b=c+d/a then
                            begin
                                if true and False then
                                    break;
                                else
                                    continue;
                            end
                        else
                            return;
                    end
                putfloatLN(1.9) ;  // error
            end

        a := 1;
    end
    """
        exp = str(UnreachableStatement(CallStmt(Id('putfloatLN'), [FloatLiteral(1.9)])))
        self.assertTrue(TestChecker.test(inp,exp,497))

    def test_all_498(self):
        """test_call_expr_param_list_must_be_type_comp"""
        inp = """
function foo(a:integer;b:real;c:strinG):boolean;
begin
    return (a*b - a/b) <= ((b / a+1) *getint());
end

procedure MaIn();
var a:boolean;
begin
    a := foo(1,2,"15gg");
    a := foo(1,2,3);  // error
end
"""
        exp = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(inp,exp,498))

    def test_all_499(self):
        """test_func_not_return5"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo5();
end
        
function foo():boolean;
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            return a=9.9;  //# return here
        end
    else
        begin
            a:=0;
            putintln(69);
            return 1.2<=1.20;  //# return here
        end
end

function foo5():boolean;  // error
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            return a=9.9;
        end
    else  //# no return
        begin
            a:=0;
            putintln(69);
        end
end
"""
        expect = str(FunctionNotReturn('foo5')) 
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_all_500(self):
        inp = """var b: integer;
                    procedure main();
                    var temp: real;
                    begin
                        temp := a();
                        putIntLn(a);
                    end

                    function a():real;
                    begin
                    end
                """
        exp = str(Undeclared(Identifier(), 'a'))
        self.assertTrue(TestChecker.test(inp,exp,500))

        

    

    

    

    




        