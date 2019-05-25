
import sys
sys.path.append('../main/mp/utils')
sys.path.append('../utils')

import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    
    def test_ast_301(self):
        input_prog = """
        procedure main();
        begin
        foo(2)[3+x] := a[b[2]] +3;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral(3),Id(r'x'))),BinaryOp('+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(3)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 301))
        
    def test_ast_302(self):
        input_prog = """
        procedure main();
        begin
        call(1, call2("xyz", 3 + 5 - not 4 or 3 / 1.3e99 * 1.5, true, false),
        calle(a[17], true + false, a["sai"]));
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'call'),[IntLiteral(1),CallExpr(Id(r'call2'),[StringLiteral(r'xyz'),BinaryOp('or',BinaryOp('-',BinaryOp('+',IntLiteral(3),IntLiteral(5)),UnaryOp(r'not',IntLiteral(4))),BinaryOp('*',BinaryOp('/',IntLiteral(3),FloatLiteral(1.3e+99)),FloatLiteral(1.5))),BooleanLiteral(True),BooleanLiteral(False)]),CallExpr(Id(r'calle'),[ArrayCell(Id(r'a'),IntLiteral(17)),BinaryOp('+',BooleanLiteral(True),BooleanLiteral(False)),ArrayCell(Id(r'a'),StringLiteral(r'sai'))])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 302))
        
    def test_ast_303(self):
        input_prog = """procedure main();
        begin
        call();
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'call'),[])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 303))
        
    def test_ast_304(self):
        input_prog = """
        procedure main();
        begin
            g := -1.2+4.6*6 mod 7+m-f*k>4+2*5-6 div abc - - - 4 or 3 and then nhyil or t or else True;
        end
        """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'g'),BinaryOp('orelse',BinaryOp('andthen',BinaryOp('>',BinaryOp('-',BinaryOp('+',BinaryOp('+',UnaryOp(r'-',FloatLiteral(1.2)),BinaryOp('mod',BinaryOp('*',FloatLiteral(4.6),IntLiteral(6)),IntLiteral(7))),Id(r'm')),BinaryOp('*',Id(r'f'),Id(r'k'))),BinaryOp('or',BinaryOp('-',BinaryOp('-',BinaryOp('+',IntLiteral(4),BinaryOp('*',IntLiteral(2),IntLiteral(5))),BinaryOp('div',IntLiteral(6),Id(r'abc'))),UnaryOp(r'-',UnaryOp(r'-',IntLiteral(4)))),IntLiteral(3))),BinaryOp('or',Id(r'nhyil'),Id(r't'))),BooleanLiteral(True)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 304))
        
    def test_ast_305(self):
        input_prog = """procedure _main(a5: integer; hihi: array [1 .. 5] of integer);
        begin
            a := "quyxyha";
        end 
        function _main(a5: integer; concu: array [1 .. 5] of integer): real;
        begin
            a := "quyxyha";
            b := true;
        end"""
        expect = str(Program([FuncDecl(Id(r'_main'),[VarDecl(Id(r'a5'),IntType()),VarDecl(Id(r'hihi'),ArrayType(1,5,IntType()))],[],[Assign(Id(r'a'),StringLiteral(r'quyxyha'))], VoidType()),FuncDecl(Id(r'_main'),[VarDecl(Id(r'a5'),IntType()),VarDecl(Id(r'concu'),ArrayType(1,5,IntType()))],[],[Assign(Id(r'a'),StringLiteral(r'quyxyha')),Assign(Id(r'b'),BooleanLiteral(True))], FloatType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 305))
        
    def test_ast_306(self):
        input_prog = """function _main(a5: integer; concu: array [1 .. 5] of integer): integer;
            begin
                a := "quyxyha";
                b := true;
            end"""
        expect = str(Program([FuncDecl(Id(r'_main'),[VarDecl(Id(r'a5'),IntType()),VarDecl(Id(r'concu'),ArrayType(1,5,IntType()))],[],[Assign(Id(r'a'),StringLiteral(r'quyxyha')),Assign(Id(r'b'),BooleanLiteral(True))], IntType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 306))
        
    def test_ast_307(self):
        input_prog = """function _main(a5: integer; concu: array [1 .. 5] of integer): integer;
            begin
                a := "quyxyha";
                b := true;
                break;
                continue;
                return abc;
            end"""
        expect = str(Program([FuncDecl(Id(r'_main'),[VarDecl(Id(r'a5'),IntType()),VarDecl(Id(r'concu'),ArrayType(1,5,IntType()))],[],[Assign(Id(r'a'),StringLiteral(r'quyxyha')),Assign(Id(r'b'),BooleanLiteral(True)),Break(),Continue(),Return(Id(r'abc'))], IntType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 307))
        
    def test_ast_308(self):
        input_prog = """function _main(a5: integer; concu: array [1 .. 5] of integer): array [99 .. 88] of integer;
            begin
                a := "quyxyha";
                b := true;
                break;
                continue;
                return abc;
            end"""
        expect = str(Program([FuncDecl(Id(r'_main'),[VarDecl(Id(r'a5'),IntType()),VarDecl(Id(r'concu'),ArrayType(1,5,IntType()))],[],[Assign(Id(r'a'),StringLiteral(r'quyxyha')),Assign(Id(r'b'),BooleanLiteral(True)),Break(),Continue(),Return(Id(r'abc'))], ArrayType(99,88,IntType()))]))
        self.assertTrue(TestAST.test(input_prog, expect, 308))
        
    def test_ast_309(self):
        input_prog = """var i : integer ;
            function f ( ) : integer ;
            begin
                return 200;
            end
            procedure main();
            var main : integer ;
            begin
                main := f ( ) ;
                putIntLn ( main ) ;
                with i : integer ; i : integer ; f : integer ;
                do begin
                    main := f := i := 100;
                    putIntLn ( i ) ;
                    putIntLn ( main ) ;
                    putIntLn ( f ) ;
                end
                putIntLn ( main ) ;
            end
            var g : real ;"""
        expect = str(Program([VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'f'),[],[],[Return(IntLiteral(200))], IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'main'),IntType())],[Assign(Id(r'main'),CallExpr(Id(r'f'),[])),CallStmt(Id(r'putIntLn'),[Id(r'main')]),With([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'f'),IntType())],[Assign(Id(r'i'),IntLiteral(100)),Assign(Id(r'f'),Id(r'i')),Assign(Id(r'main'),Id(r'f')),CallStmt(Id(r'putIntLn'),[Id(r'i')]),CallStmt(Id(r'putIntLn'),[Id(r'main')]),CallStmt(Id(r'putIntLn'),[Id(r'f')])]),CallStmt(Id(r'putIntLn'),[Id(r'main')])], VoidType()),VarDecl(Id(r'g'),FloatType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 309))
        
    def test_ast_310(self):
        input_prog = """procedure main();
        begin
        if a + 4 - 7 * 5 or 3 then
            begin
                break;
                continue;
                return;
            end
        else
            if a or true - 9 + 3 then
                begin
                    b := ansnd + 151 + 47 * 3;
                    break;
                    continue;
                    return 19;
                end
            else
                begin
                    return 12-13;
                    if a then
                        return "asdausdasd";
                    else
                        begin
                            continue;
                            return 1-33;
                            if b then
                                ko := id;
                            else
                                return a;
                        end

                    
                end
            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp('or',BinaryOp('-',BinaryOp('+',Id(r'a'),IntLiteral(4)),BinaryOp('*',IntLiteral(7),IntLiteral(5))),IntLiteral(3)),[Break(),Continue(),Return()],[If(BinaryOp('+',BinaryOp('-',BinaryOp('or',Id(r'a'),BooleanLiteral(True)),IntLiteral(9)),IntLiteral(3)),[Assign(Id(r'b'),BinaryOp('+',BinaryOp('+',Id(r'ansnd'),IntLiteral(151)),BinaryOp('*',IntLiteral(47),IntLiteral(3)))),Break(),Continue(),Return(IntLiteral(19))],[Return(BinaryOp('-',IntLiteral(12),IntLiteral(13))),If(Id(r'a'),[Return(StringLiteral(r'asdausdasd'))],[Continue(),Return(BinaryOp('-',IntLiteral(1),IntLiteral(33))),If(Id(r'b'),[Assign(Id(r'ko'),Id(r'id'))],[Return(Id(r'a'))])])])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 310))
        
    def test_ast_311(self):
        input_prog = """
        procedure main();
        Begin
            Write("HelloWorld.PreparetolearnPASCAL!!");
        End"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Write'),[StringLiteral(r'HelloWorld.PreparetolearnPASCAL!!')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 311))
        
    def test_ast_312(self):
        input_prog = """
        procedure main();
        Var       
            Num1, Num2, Sum : Integer;
        begin
        
        Begin {no semicolon}
            Write("Inputnumber1:"); 
            Readln(Num1);
            Writeln("Inputnumber2:");
            Readln(Num2);
            Sum := Num1 + Num2; {addition} 
            Writeln(Sum);
        End
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'Num1'),IntType()),VarDecl(Id(r'Num2'),IntType()),VarDecl(Id(r'Sum'),IntType())],[CallStmt(Id(r'Write'),[StringLiteral(r'Inputnumber1:')]),CallStmt(Id(r'Readln'),[Id(r'Num1')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'Inputnumber2:')]),CallStmt(Id(r'Readln'),[Id(r'Num2')]),Assign(Id(r'Sum'),BinaryOp('+',Id(r'Num1'),Id(r'Num2'))),CallStmt(Id(r'Writeln'),[Id(r'Sum')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 312))
        
    def test_ast_313(self):
        input_prog = """
        var RoundRealRate : integer;

            {******************************************************************}
            {* Print message, release resources and reset environment         *}
            {******************************************************************}
            procedure Restore ( Message: string;
                                ReturnCode: integer );
            begin
                Write(Message);
                if ReturnCode <> OK then
                {*   Write(SayCalRe(ReturnCode));
                Writeln("");                   *}
                    Msg1(Output,1, addr(SayCalRe(ReturnCode)) );
                else Msg0(Output, 2);

                break;
                Close (Input);
                Close (Output);
            end
        """
        expect = str(Program([VarDecl(Id(r'RoundRealRate'),IntType()),FuncDecl(Id(r'Restore'),[VarDecl(Id(r'Message'),StringType()),VarDecl(Id(r'ReturnCode'),IntType())],[],[CallStmt(Id(r'Write'),[Id(r'Message')]),If(BinaryOp('<>',Id(r'ReturnCode'),Id(r'OK')),[CallStmt(Id(r'Msg1'),[Id(r'Output'),IntLiteral(1),CallExpr(Id(r'addr'),[CallExpr(Id(r'SayCalRe'),[Id(r'ReturnCode')])])])],[CallStmt(Id(r'Msg0'),[Id(r'Output'),IntLiteral(2)])]),Break(),CallStmt(Id(r'Close'),[Id(r'Input')]),CallStmt(Id(r'Close'),[Id(r'Output')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 313))
        
    def test_ast_314(self):
        input_prog = """procedure main();
        begin
        if ReturnCode <> OK then
            {*   Write(SayCalRe(ReturnCode));
            Writeln("");                   *}
                Msg1(Output,1, addr(SayCalRe(ReturnCode)) );
            else Msg0(Output, 2);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp('<>',Id(r'ReturnCode'),Id(r'OK')),[CallStmt(Id(r'Msg1'),[Id(r'Output'),IntLiteral(1),CallExpr(Id(r'addr'),[CallExpr(Id(r'SayCalRe'),[Id(r'ReturnCode')])])])],[CallStmt(Id(r'Msg0'),[Id(r'Output'),IntLiteral(2)])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 314))
        
    def test_ast_315(self):
        input_prog = """
        procedure main();
        begin
        x := not abc(GetIPAddr(Trim(Ltrim(Line)), HostAddress,
                     AddrSpec, Lookup));
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'x'),UnaryOp(r'not',CallExpr(Id(r'abc'),[CallExpr(Id(r'GetIPAddr'),[CallExpr(Id(r'Trim'),[CallExpr(Id(r'Ltrim'),[Id(r'Line')])]),Id(r'HostAddress'),Id(r'AddrSpec'),Id(r'Lookup')])])))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 315))
        
    def test_ast_316(self):
        input_prog = """
        procedure main();
        begin
        with a ,b: integer ; c : array [ 1 .. 2 ] of real ; do
            d := c[a] + b;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp('+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b')))])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 316))
        
    def test_ast_317(self):
        input_prog = """function foo (): real ;
            begin
                if a then return 2.3; // CORRECT
                else return 2; // CORRECT
            end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[If(Id(r'a'),[Return(FloatLiteral(2.3))],[Return(IntLiteral(2))])], FloatType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 317))
        
    def test_ast_318(self):
        input_prog = """function foo (b: array [ 1 .. 2 ] of integer ): array [2 .. 3] of real ;
            var
            a : array [2 .. 3] of real ;
            begin
            if (a) then return a ; //CORRECT
            else return b; //WRONG
            end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'b'),ArrayType(1,2,IntType()))],[VarDecl(Id(r'a'),ArrayType(2,3,FloatType()))],[If(Id(r'a'),[Return(Id(r'a'))],[Return(Id(r'b'))])], ArrayType(2,3,FloatType()))]))
        self.assertTrue(TestAST.test(input_prog, expect, 318))
        
    def test_ast_319(self):
        input_prog = """procedure main();
        begin
        foo(2)[3+x] := a[b[2]] +3; (* ahsdiuahsidh *)
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral(3),Id(r'x'))),BinaryOp('+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(3)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 319))
        
    def test_ast_320(self):
        input_prog = """procedure main();
        begin
        a := - true; // aHihi
            b := - 15; (* how about this *)
            b := - 15;
        end { so this }"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),UnaryOp(r'-',BooleanLiteral(True))),Assign(Id(r'b'),UnaryOp(r'-',IntLiteral(15))),Assign(Id(r'b'),UnaryOp(r'-',IntLiteral(15)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 320))
        
    def test_ast_321(self):
        input_prog = """
        procedure main();
        begin
		read(character);
		charcount := charcount + 1;
		if character = BLANK
			then blankcount := blankcount + 1;
		else if character = COMMA
			then commacount := commacount + 1;
		else if character = PERIOD
			then periodcount := periodcount + 1;
	end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'character')]),Assign(Id(r'charcount'),BinaryOp('+',Id(r'charcount'),IntLiteral(1))),If(BinaryOp('=',Id(r'character'),Id(r'BLANK')),[Assign(Id(r'blankcount'),BinaryOp('+',Id(r'blankcount'),IntLiteral(1)))],[If(BinaryOp('=',Id(r'character'),Id(r'COMMA')),[Assign(Id(r'commacount'),BinaryOp('+',Id(r'commacount'),IntLiteral(1)))],[If(BinaryOp('=',Id(r'character'),Id(r'PERIOD')),[Assign(Id(r'periodcount'),BinaryOp('+',Id(r'periodcount'),IntLiteral(1)))],[])])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 321))
        
    def test_ast_322(self):
        input_prog = """
        procedure main();
        var
            charcount, blankcount, commacount, periodcount: integer;
            character : real;
        begin
            
            
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'charcount'),IntType()),VarDecl(Id(r'blankcount'),IntType()),VarDecl(Id(r'commacount'),IntType()),VarDecl(Id(r'periodcount'),IntType()),VarDecl(Id(r'character'),FloatType())],[], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 322))
        
    def test_ast_323(self):
        input_prog = """
        procedure main();
        var
            oldchar, newchar: integer;
        begin
            oldchar := BLANK;
            while not eof do
            begin
                read(newchar);
                if (newchar <> BLANK) and (oldchar = newchar)
                    then writeln(oldchar, newchar);
                oldchar := newchar;			
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'oldchar'),IntType()),VarDecl(Id(r'newchar'),IntType())],[Assign(Id(r'oldchar'),Id(r'BLANK')),While(UnaryOp(r'not',Id(r'eof')),[CallStmt(Id(r'read'),[Id(r'newchar')]),If(BinaryOp('and',BinaryOp('<>',Id(r'newchar'),Id(r'BLANK')),BinaryOp('=',Id(r'oldchar'),Id(r'newchar'))),[CallStmt(Id(r'writeln'),[Id(r'oldchar'),Id(r'newchar')])],[]),Assign(Id(r'oldchar'),Id(r'newchar'))])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 323))
        
    def test_ast_324(self):
        input_prog = """
        procedure main();
        var
            inches, cent: Real;
        (* This is a comment *)
        begin
            write("Enteralengthininches:");
            readln(inches);
            cent := CENT_PER_INCH * inches;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'inches'),FloatType()),VarDecl(Id(r'cent'),FloatType())],[CallStmt(Id(r'write'),[StringLiteral(r'Enteralengthininches:')]),CallStmt(Id(r'readln'),[Id(r'inches')]),Assign(Id(r'cent'),BinaryOp('*',Id(r'CENT_PER_INCH'),Id(r'inches')))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 324))
        
    def test_ast_325(self):
        input_prog = """procedure main();
                        begin
                        if number = 0
                            then reading := false;
                        else
                            begin
                                count := count + 1;
                                if number < min
                                    then min := number;
                                if number > max
                                    then max := number;
                            end
                        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp('=',Id(r'number'),IntLiteral(0)),[Assign(Id(r'reading'),BooleanLiteral(False))],[Assign(Id(r'count'),BinaryOp('+',Id(r'count'),IntLiteral(1))),If(BinaryOp('<',Id(r'number'),Id(r'min')),[Assign(Id(r'min'),Id(r'number'))],[]),If(BinaryOp('>',Id(r'number'),Id(r'max')),[Assign(Id(r'max'),Id(r'number'))],[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 325))
        
    def test_ast_326(self):
        input_prog = """procedure main();
                        begin
                    for base := 1 to tableSize do
                    begin
                        square := sqr(base);
                        cube := base * square;
                        quad := sqr(square);
                        writeln(base, square, cube, quad, 1/base, 1/square,
                            1/cube, 1/quad);
                                
                    end
                    end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'base'),IntLiteral(1),Id(r'tableSize'),True,[Assign(Id(r'square'),CallExpr(Id(r'sqr'),[Id(r'base')])),Assign(Id(r'cube'),BinaryOp('*',Id(r'base'),Id(r'square'))),Assign(Id(r'quad'),CallExpr(Id(r'sqr'),[Id(r'square')])),CallStmt(Id(r'writeln'),[Id(r'base'),Id(r'square'),Id(r'cube'),Id(r'quad'),BinaryOp('/',IntLiteral(1),Id(r'base')),BinaryOp('/',IntLiteral(1),Id(r'square')),BinaryOp('/',IntLiteral(1),Id(r'cube')),BinaryOp('/',IntLiteral(1),Id(r'quad'))])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 326))
        
    def test_ast_327(self):
        input_prog = """
        procedure main();
                        begin
                        write("Enteranumber:" );
                    read(x);
                    if x >= 0
                        then writeln(sqrt(x));
                        else writeln(x, "Doesnothavearealsquareroot.");	
                    end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Enteranumber:')]),CallStmt(Id(r'read'),[Id(r'x')]),If(BinaryOp('>=',Id(r'x'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[CallExpr(Id(r'sqrt'),[Id(r'x')])])],[CallStmt(Id(r'writeln'),[Id(r'x'),StringLiteral(r'Doesnothavearealsquareroot.')])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 327))
        
    def test_ast_328(self):
        input_prog = """procedure who(input: real; output: Integer);
        var
            name: array [1 .. 20] of real;
            letter: Integer;
        begin
            write("Whatsyourname?:");
            for letter := 1 to 20 do 
                read(name[letter]);
            writeln(name);
        end"""
        expect = str(Program([FuncDecl(Id(r'who'),[VarDecl(Id(r'input'),FloatType()),VarDecl(Id(r'output'),IntType())],[VarDecl(Id(r'name'),ArrayType(1,20,FloatType())),VarDecl(Id(r'letter'),IntType())],[CallStmt(Id(r'write'),[StringLiteral(r'Whatsyourname?:')]),For(Id(r'letter'),IntLiteral(1),IntLiteral(20),True,[CallStmt(Id(r'read'),[ArrayCell(Id(r'name'),Id(r'letter'))])]),CallStmt(Id(r'writeln'),[Id(r'name')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 328))
        
    def test_ast_329(self):
        input_prog = """function assignments(output: real):real ;
        var
            period: real;
            gravitational_force : real;

        begin
            period := 2 * pi * sqrt(15/9.81);
            gravitational_force := (6.673E-8 * 34 * 65) / sqr(9);
            writeln(gravitational_force);
        end"""
        expect = str(Program([FuncDecl(Id(r'assignments'),[VarDecl(Id(r'output'),FloatType())],[VarDecl(Id(r'period'),FloatType()),VarDecl(Id(r'gravitational_force'),FloatType())],[Assign(Id(r'period'),BinaryOp('*',BinaryOp('*',IntLiteral(2),Id(r'pi')),CallExpr(Id(r'sqrt'),[BinaryOp('/',IntLiteral(15),FloatLiteral(9.81))]))),Assign(Id(r'gravitational_force'),BinaryOp('/',BinaryOp('*',BinaryOp('*',FloatLiteral(6.673e-08),IntLiteral(34)),IntLiteral(65)),CallExpr(Id(r'sqr'),[IntLiteral(9)]))),CallStmt(Id(r'writeln'),[Id(r'gravitational_force')])], FloatType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 329))
        
    def test_ast_330(self):
        input_prog = """procedure expressions();
        {}
        begin
            writeln(pred(5), succ(5));
            writeln(pred(5), abs(-4));
            writeln(pred(5), sqr(-4));
            writeln(sin(pi), sqr(-4));
            writeln(succ("a"));
        end"""
        expect = str(Program([FuncDecl(Id(r'expressions'),[],[],[CallStmt(Id(r'writeln'),[CallExpr(Id(r'pred'),[IntLiteral(5)]),CallExpr(Id(r'succ'),[IntLiteral(5)])]),CallStmt(Id(r'writeln'),[CallExpr(Id(r'pred'),[IntLiteral(5)]),CallExpr(Id(r'abs'),[UnaryOp(r'-',IntLiteral(4))])]),CallStmt(Id(r'writeln'),[CallExpr(Id(r'pred'),[IntLiteral(5)]),CallExpr(Id(r'sqr'),[UnaryOp(r'-',IntLiteral(4))])]),CallStmt(Id(r'writeln'),[CallExpr(Id(r'sin'),[Id(r'pi')]),CallExpr(Id(r'sqr'),[UnaryOp(r'-',IntLiteral(4))])]),CallStmt(Id(r'writeln'),[CallExpr(Id(r'succ'),[StringLiteral(r'a')])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 330))
        
    def test_ast_331(self):
        input_prog = """procedure pas();
        var
            x : integer;
        begin
            write(":");
            read(x);
            if x < 0 then 
                x := -x;
            writeln(x);	
        end"""
        expect = str(Program([FuncDecl(Id(r'pas'),[],[VarDecl(Id(r'x'),IntType())],[CallStmt(Id(r'write'),[StringLiteral(r':')]),CallStmt(Id(r'read'),[Id(r'x')]),If(BinaryOp('<',Id(r'x'),IntLiteral(0)),[Assign(Id(r'x'),UnaryOp(r'-',Id(r'x')))],[]),CallStmt(Id(r'writeln'),[Id(r'x')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 331))
        
    def test_ast_332(self):
        input_prog = """procedure average();
        var
            count : integer;
            sum, current : real;
            avg : real;
        begin
            current := 0.0;
            sum := 0.0;
            count := 0;
            while current <> END_OF_DATA do
            begin
                read(current);
                sum := sum + current;
                count := succ(count);		
            end
            avg := sum / (count + 0.0);
            writeln("AVERAGE:", avg);
        end"""
        expect = str(Program([FuncDecl(Id(r'average'),[],[VarDecl(Id(r'count'),IntType()),VarDecl(Id(r'sum'),FloatType()),VarDecl(Id(r'current'),FloatType()),VarDecl(Id(r'avg'),FloatType())],[Assign(Id(r'current'),FloatLiteral(0.0)),Assign(Id(r'sum'),FloatLiteral(0.0)),Assign(Id(r'count'),IntLiteral(0)),While(BinaryOp('<>',Id(r'current'),Id(r'END_OF_DATA')),[CallStmt(Id(r'read'),[Id(r'current')]),Assign(Id(r'sum'),BinaryOp('+',Id(r'sum'),Id(r'current'))),Assign(Id(r'count'),CallExpr(Id(r'succ'),[Id(r'count')]))]),Assign(Id(r'avg'),BinaryOp('/',Id(r'sum'),BinaryOp('+',Id(r'count'),FloatLiteral(0.0)))),CallStmt(Id(r'writeln'),[StringLiteral(r'AVERAGE:'),Id(r'avg')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 332))
        
    def test_ast_333(self):
        input_prog = """procedure main();
        begin
            readln(number);
            product := number;
            counter := 0;
            if number <> 0 then
                while not odd(number) do
                    begin
                        number := number div 2;
                        counter := succ(counter);
                    end
            writeln("Final:", number);
            writeln("Loop:", counter);
            if counter = 1 then
                writeln(2,number, product);
            else
                begin
                    factor := product div number;
                    writeln(2,number, product);
                end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'readln'),[Id(r'number')]),Assign(Id(r'product'),Id(r'number')),Assign(Id(r'counter'),IntLiteral(0)),If(BinaryOp('<>',Id(r'number'),IntLiteral(0)),[While(UnaryOp(r'not',CallExpr(Id(r'odd'),[Id(r'number')])),[Assign(Id(r'number'),BinaryOp('div',Id(r'number'),IntLiteral(2))),Assign(Id(r'counter'),CallExpr(Id(r'succ'),[Id(r'counter')]))])],[]),CallStmt(Id(r'writeln'),[StringLiteral(r'Final:'),Id(r'number')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Loop:'),Id(r'counter')]),If(BinaryOp('=',Id(r'counter'),IntLiteral(1)),[CallStmt(Id(r'writeln'),[IntLiteral(2),Id(r'number'),Id(r'product')])],[Assign(Id(r'factor'),BinaryOp('div',Id(r'product'),Id(r'number'))),CallStmt(Id(r'writeln'),[IntLiteral(2),Id(r'number'),Id(r'product')])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 333))
        
    def test_ast_334(self):
        input_prog = """
        procedure main();
                    
        begin
            write("Rows:");
            read(rows);
            lastNumber := 1;
            for i := 1 to rows do
            begin
                for j := 1 to i do
                begin
                    write(lastNumber);
                    lastNumber := succ(lastNumber) mod 2;			
                end
                writeln();		
            end	
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Rows:')]),CallStmt(Id(r'read'),[Id(r'rows')]),Assign(Id(r'lastNumber'),IntLiteral(1)),For(Id(r'i'),IntLiteral(1),Id(r'rows'),True,[For(Id(r'j'),IntLiteral(1),Id(r'i'),True,[CallStmt(Id(r'write'),[Id(r'lastNumber')]),Assign(Id(r'lastNumber'),BinaryOp('mod',CallExpr(Id(r'succ'),[Id(r'lastNumber')]),IntLiteral(2)))]),CallStmt(Id(r'writeln'),[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 334))
        
    def test_ast_335(self):
        input_prog = """procedure main();
                        begin
            writeln("Countdownhasbegun");
            sec := 10;
                sec := sec - 1;	
            writeln("Zero");
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'writeln'),[StringLiteral(r'Countdownhasbegun')]),Assign(Id(r'sec'),IntLiteral(10)),Assign(Id(r'sec'),BinaryOp('-',Id(r'sec'),IntLiteral(1))),CallStmt(Id(r'writeln'),[StringLiteral(r'Zero')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 335))
        
    def test_ast_336(self):
        input_prog = """procedure main();
                        begin
            write("n:");
            read(number);
            for i := 0 to number do
                if (i mod 2 = 0) then
                    write(i, "");
            writeln();
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'n:')]),CallStmt(Id(r'read'),[Id(r'number')]),For(Id(r'i'),IntLiteral(0),Id(r'number'),True,[If(BinaryOp('=',BinaryOp('mod',Id(r'i'),IntLiteral(2)),IntLiteral(0)),[CallStmt(Id(r'write'),[Id(r'i'),StringLiteral(r'')])],[])]),CallStmt(Id(r'writeln'),[])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 336))
        
    def test_ast_337(self):
        input_prog = """procedure main();
                    
                        begin
            read(number);
            fact := 1;
            for i := number downto 1 do
            begin
                fact := fact * i;		
            end
            writeln(fact);
            {}
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'number')]),Assign(Id(r'fact'),IntLiteral(1)),For(Id(r'i'),Id(r'number'),IntLiteral(1),False,[Assign(Id(r'fact'),BinaryOp('*',Id(r'fact'),Id(r'i')))]),CallStmt(Id(r'writeln'),[Id(r'fact')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 337))
        
    def test_ast_338(self):
        input_prog = """procedure main();
                        begin
            write("Rows:");
            read(rows);
            lastNumber := 1;
            for i := 1 to rows do
            begin
                for j := 1 to i do
                begin
                    write(lastNumber);
                    lastNumber := succ(lastNumber);			
                end
                writeln();		
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Rows:')]),CallStmt(Id(r'read'),[Id(r'rows')]),Assign(Id(r'lastNumber'),IntLiteral(1)),For(Id(r'i'),IntLiteral(1),Id(r'rows'),True,[For(Id(r'j'),IntLiteral(1),Id(r'i'),True,[CallStmt(Id(r'write'),[Id(r'lastNumber')]),Assign(Id(r'lastNumber'),CallExpr(Id(r'succ'),[Id(r'lastNumber')]))]),CallStmt(Id(r'writeln'),[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 338))
        
    def test_ast_339(self):
        input_prog = """procedure main();
                        begin
            read(a, b);
            while (a > 0) and (b > 0) do
            begin
                tempa := a; 
                tempb := b;
                rem := a mod b;
                while rem > 0 do
                begin
                    b := a;
                    a := rem;
                    rem := b mod a;
                end
                writeln(a);
                read(a, b);
            end
            {}
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'a'),Id(r'b')]),While(BinaryOp('and',BinaryOp('>',Id(r'a'),IntLiteral(0)),BinaryOp('>',Id(r'b'),IntLiteral(0))),[Assign(Id(r'tempa'),Id(r'a')),Assign(Id(r'tempb'),Id(r'b')),Assign(Id(r'rem'),BinaryOp('mod',Id(r'a'),Id(r'b'))),While(BinaryOp('>',Id(r'rem'),IntLiteral(0)),[Assign(Id(r'b'),Id(r'a')),Assign(Id(r'a'),Id(r'rem')),Assign(Id(r'rem'),BinaryOp('mod',Id(r'b'),Id(r'a')))]),CallStmt(Id(r'writeln'),[Id(r'a')]),CallStmt(Id(r'read'),[Id(r'a'),Id(r'b')])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 339))
        
    def test_ast_340(self):
        input_prog = """procedure main();
                        begin
            termcount := 0;
            sum := 0;
            read(limit);
                termcount := succ(termcount);
                sum := sum + (1 / termcount);		
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'termcount'),IntLiteral(0)),Assign(Id(r'sum'),IntLiteral(0)),CallStmt(Id(r'read'),[Id(r'limit')]),Assign(Id(r'termcount'),CallExpr(Id(r'succ'),[Id(r'termcount')])),Assign(Id(r'sum'),BinaryOp('+',Id(r'sum'),BinaryOp('/',IntLiteral(1),Id(r'termcount'))))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 340))
        
    def test_ast_341(self):
        input_prog = """procedure main();
                        begin
            summation := 0;
            variable := 0;
            while(summation <= BOUND) do
            begin
                summation := summation + variable * variable * variable;
                variable := succ(variable);		
            end
            writeln(variable);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'summation'),IntLiteral(0)),Assign(Id(r'variable'),IntLiteral(0)),While(BinaryOp('<=',Id(r'summation'),Id(r'BOUND')),[Assign(Id(r'summation'),BinaryOp('+',Id(r'summation'),BinaryOp('*',BinaryOp('*',Id(r'variable'),Id(r'variable')),Id(r'variable')))),Assign(Id(r'variable'),CallExpr(Id(r'succ'),[Id(r'variable')]))]),CallStmt(Id(r'writeln'),[Id(r'variable')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 341))
        
    def test_ast_342(self):
        input_prog = """procedure main();
                        begin
            read(a, b, n);
            h := (b - a) / (fk(n));
            point := a;
            summation := 0;
            for i := 1 to n do
            begin
                point := point + h;
                term := log10(point + h) + log10(point);
                summation := summation + term;		
            end
            summation := (h / 2.0) * summation;
            writeln(summation);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'a'),Id(r'b'),Id(r'n')]),Assign(Id(r'h'),BinaryOp('/',BinaryOp('-',Id(r'b'),Id(r'a')),CallExpr(Id(r'fk'),[Id(r'n')]))),Assign(Id(r'point'),Id(r'a')),Assign(Id(r'summation'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[Assign(Id(r'point'),BinaryOp('+',Id(r'point'),Id(r'h'))),Assign(Id(r'term'),BinaryOp('+',CallExpr(Id(r'log10'),[BinaryOp('+',Id(r'point'),Id(r'h'))]),CallExpr(Id(r'log10'),[Id(r'point')]))),Assign(Id(r'summation'),BinaryOp('+',Id(r'summation'),Id(r'term')))]),Assign(Id(r'summation'),BinaryOp('*',BinaryOp('/',Id(r'h'),FloatLiteral(2.0)),Id(r'summation'))),CallStmt(Id(r'writeln'),[Id(r'summation')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 342))
        
    def test_ast_343(self):
        input_prog = """procedure main();
                        begin
            read(number);
            counter := 1;
            while (counter <> MAX) do
            begin
                writeln(number, "*", counter, "=", number * counter);
                counter := succ(counter);
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'number')]),Assign(Id(r'counter'),IntLiteral(1)),While(BinaryOp('<>',Id(r'counter'),Id(r'MAX')),[CallStmt(Id(r'writeln'),[Id(r'number'),StringLiteral(r'*'),Id(r'counter'),StringLiteral(r'='),BinaryOp('*',Id(r'number'),Id(r'counter'))]),Assign(Id(r'counter'),CallExpr(Id(r'succ'),[Id(r'counter')]))])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 343))
        
    def test_ast_344(self):
        input_prog = """procedure main();
                        begin
            write("n:");
            read(number);
            for i := 0 to number do
                if (i mod 2 <> 0) then
                    write(i);
            writeln();
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'n:')]),CallStmt(Id(r'read'),[Id(r'number')]),For(Id(r'i'),IntLiteral(0),Id(r'number'),True,[If(BinaryOp('<>',BinaryOp('mod',Id(r'i'),IntLiteral(2)),IntLiteral(0)),[CallStmt(Id(r'write'),[Id(r'i')])],[])]),CallStmt(Id(r'writeln'),[])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 344))
        
    def test_ast_345(self):
        input_prog = """procedure main();
                        begin
                distribution := 0.0;
                factorial := 1;
                result := 1.0;
                x := i;
                lambda := realn(x) / 2.0;
                for j := 1 to x do
                    result := result * lambda;
                for j := 1 to x do
                    factorial := factorial * j;
                distribution := (result / factorial) * exp(-lambda);
                writeln(distribution);
                i := succ(i);
            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'distribution'),FloatLiteral(0.0)),Assign(Id(r'factorial'),IntLiteral(1)),Assign(Id(r'result'),FloatLiteral(1.0)),Assign(Id(r'x'),Id(r'i')),Assign(Id(r'lambda'),BinaryOp('/',CallExpr(Id(r'realn'),[Id(r'x')]),FloatLiteral(2.0))),For(Id(r'j'),IntLiteral(1),Id(r'x'),True,[Assign(Id(r'result'),BinaryOp('*',Id(r'result'),Id(r'lambda')))]),For(Id(r'j'),IntLiteral(1),Id(r'x'),True,[Assign(Id(r'factorial'),BinaryOp('*',Id(r'factorial'),Id(r'j')))]),Assign(Id(r'distribution'),BinaryOp('*',BinaryOp('/',Id(r'result'),Id(r'factorial')),CallExpr(Id(r'exp'),[UnaryOp(r'-',Id(r'lambda'))]))),CallStmt(Id(r'writeln'),[Id(r'distribution')]),Assign(Id(r'i'),CallExpr(Id(r'succ'),[Id(r'i')]))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 345))
        
    def test_ast_346(self):
        input_prog = """procedure main();
                        begin
            write("n:");
            read(number);
            for i := 0 to number do
            begin
                for j := 0 to number do
                    write("+");
                write(" ");
                for j := 0 to number do
                    write("+");
                writeln();
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'n:')]),CallStmt(Id(r'read'),[Id(r'number')]),For(Id(r'i'),IntLiteral(0),Id(r'number'),True,[For(Id(r'j'),IntLiteral(0),Id(r'number'),True,[CallStmt(Id(r'write'),[StringLiteral(r'+')])]),CallStmt(Id(r'write'),[StringLiteral(r' ')]),For(Id(r'j'),IntLiteral(0),Id(r'number'),True,[CallStmt(Id(r'write'),[StringLiteral(r'+')])]),CallStmt(Id(r'writeln'),[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 346))
        
    def test_ast_347(self):
        input_prog = """procedure main();
                        begin
            write("N:");
            read(n);
            sum := 0.0;
            accum := 2;
            for i := 0 to n do
            begin
                accum := accum * 2;
                sum := sum + (i / accum);		
            end
            writeln("Sum:", sum);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'N:')]),CallStmt(Id(r'read'),[Id(r'n')]),Assign(Id(r'sum'),FloatLiteral(0.0)),Assign(Id(r'accum'),IntLiteral(2)),For(Id(r'i'),IntLiteral(0),Id(r'n'),True,[Assign(Id(r'accum'),BinaryOp('*',Id(r'accum'),IntLiteral(2))),Assign(Id(r'sum'),BinaryOp('+',Id(r'sum'),BinaryOp('/',Id(r'i'),Id(r'accum'))))]),CallStmt(Id(r'writeln'),[StringLiteral(r'Sum:'),Id(r'sum')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 347))
        
    def test_ast_348(self):
        input_prog = """procedure main();
                        begin
            write("SIZE:");
            read(size);
            for i := 1 to size do
            begin
                for j := 1 to i do
                    write(PATT);
                writeln();
            end
            for i := size downto 1 do
            begin
                for j := i downto 1 do
                    write(PATT);
                writeln();
        end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'SIZE:')]),CallStmt(Id(r'read'),[Id(r'size')]),For(Id(r'i'),IntLiteral(1),Id(r'size'),True,[For(Id(r'j'),IntLiteral(1),Id(r'i'),True,[CallStmt(Id(r'write'),[Id(r'PATT')])]),CallStmt(Id(r'writeln'),[])]),For(Id(r'i'),Id(r'size'),IntLiteral(1),False,[For(Id(r'j'),Id(r'i'),IntLiteral(1),False,[CallStmt(Id(r'write'),[Id(r'PATT')])]),CallStmt(Id(r'writeln'),[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 348))
        
    def test_ast_349(self):
        input_prog = """procedure main();
                        begin
            write("SIZE:");
            read(size);
            pattern2 := size - 1;
            pattern1 := size - pattern2; 
            for i := 0 to size do
            begin
                for j := 0 to pattern1 - 1 do
                    write(DOTS);
                for k := 0 to pattern2 do
                    write(LINES);
                pattern1 := succ(pattern1);
                pattern2 := pred(pattern2);
                writeln(); 	
            end	
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'SIZE:')]),CallStmt(Id(r'read'),[Id(r'size')]),Assign(Id(r'pattern2'),BinaryOp('-',Id(r'size'),IntLiteral(1))),Assign(Id(r'pattern1'),BinaryOp('-',Id(r'size'),Id(r'pattern2'))),For(Id(r'i'),IntLiteral(0),Id(r'size'),True,[For(Id(r'j'),IntLiteral(0),BinaryOp('-',Id(r'pattern1'),IntLiteral(1)),True,[CallStmt(Id(r'write'),[Id(r'DOTS')])]),For(Id(r'k'),IntLiteral(0),Id(r'pattern2'),True,[CallStmt(Id(r'write'),[Id(r'LINES')])]),Assign(Id(r'pattern1'),CallExpr(Id(r'succ'),[Id(r'pattern1')])),Assign(Id(r'pattern2'),CallExpr(Id(r'pred'),[Id(r'pattern2')])),CallStmt(Id(r'writeln'),[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 349))
        
    def test_ast_350(self):
        input_prog = """procedure main();
                        begin
            write("Size:");
            read(size);
            for i := 0 to size do
                write("*");
            writeln();
            for i := 0 to (size - 1) do
            begin
                write("*");
                for j := 0 to (size - 2) do
                    write("");
                write("*");
                writeln();
            end
            for i := 0 to size do
                write("*");
            writeln();
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Size:')]),CallStmt(Id(r'read'),[Id(r'size')]),For(Id(r'i'),IntLiteral(0),Id(r'size'),True,[CallStmt(Id(r'write'),[StringLiteral(r'*')])]),CallStmt(Id(r'writeln'),[]),For(Id(r'i'),IntLiteral(0),BinaryOp('-',Id(r'size'),IntLiteral(1)),True,[CallStmt(Id(r'write'),[StringLiteral(r'*')]),For(Id(r'j'),IntLiteral(0),BinaryOp('-',Id(r'size'),IntLiteral(2)),True,[CallStmt(Id(r'write'),[StringLiteral(r'')])]),CallStmt(Id(r'write'),[StringLiteral(r'*')]),CallStmt(Id(r'writeln'),[])]),For(Id(r'i'),IntLiteral(0),Id(r'size'),True,[CallStmt(Id(r'write'),[StringLiteral(r'*')])]),CallStmt(Id(r'writeln'),[])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 350))
        
    def test_ast_351(self):
        input_prog = """procedure main();
                        begin
            number := 5.0;
            sum := 0.0;
            count := 0;
            while (number <> 0) do
            begin
                read(number);
                sum := sum + number;
                count := succ(count);		
            end
            count := pred(count);
            writeln("Mean:", (sum / count));
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'number'),FloatLiteral(5.0)),Assign(Id(r'sum'),FloatLiteral(0.0)),Assign(Id(r'count'),IntLiteral(0)),While(BinaryOp('<>',Id(r'number'),IntLiteral(0)),[CallStmt(Id(r'read'),[Id(r'number')]),Assign(Id(r'sum'),BinaryOp('+',Id(r'sum'),Id(r'number'))),Assign(Id(r'count'),CallExpr(Id(r'succ'),[Id(r'count')]))]),Assign(Id(r'count'),CallExpr(Id(r'pred'),[Id(r'count')])),CallStmt(Id(r'writeln'),[StringLiteral(r'Mean:'),BinaryOp('/',Id(r'sum'),Id(r'count'))])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 351))
        
    def test_ast_352(self):
        input_prog = """procedure main();
                    begin
            write("Number:");
            read(number);
            if number < 0 then
                writeln();
            else
                begin
                    flag := number;
                    sum := 0;
                    digit := 0;
                    while (number > 0) do
                        begin
                            digit := number mod 10;
                            sum := sum + digit;
                            number := number div 10;				
                        end
                end	
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Number:')]),CallStmt(Id(r'read'),[Id(r'number')]),If(BinaryOp('<',Id(r'number'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[])],[Assign(Id(r'flag'),Id(r'number')),Assign(Id(r'sum'),IntLiteral(0)),Assign(Id(r'digit'),IntLiteral(0)),While(BinaryOp('>',Id(r'number'),IntLiteral(0)),[Assign(Id(r'digit'),BinaryOp('mod',Id(r'number'),IntLiteral(10))),Assign(Id(r'sum'),BinaryOp('+',Id(r'sum'),Id(r'digit'))),Assign(Id(r'number'),BinaryOp('div',Id(r'number'),IntLiteral(10)))])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 352))
        
    def test_ast_353(self):
        input_prog = """procedure main();
                        begin
            for n := 1 to (maxint - 1) do
            begin
                left := 1 / (n + 1);
                center := ln((n + 1) / n);
                rigth := 1 / n;
                writeln(n, (left < center)  and (center < rigth));		
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'n'),IntLiteral(1),BinaryOp('-',Id(r'maxint'),IntLiteral(1)),True,[Assign(Id(r'left'),BinaryOp('/',IntLiteral(1),BinaryOp('+',Id(r'n'),IntLiteral(1)))),Assign(Id(r'center'),CallExpr(Id(r'ln'),[BinaryOp('/',BinaryOp('+',Id(r'n'),IntLiteral(1)),Id(r'n'))])),Assign(Id(r'rigth'),BinaryOp('/',IntLiteral(1),Id(r'n'))),CallStmt(Id(r'writeln'),[Id(r'n'),BinaryOp('and',BinaryOp('<',Id(r'left'),Id(r'center')),BinaryOp('<',Id(r'center'),Id(r'rigth')))])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 353))
        
    def test_ast_354(self):
        input_prog = """procedure main();
                        begin
            write("Size:");
            read(size);
            spaces := size;
            spots := 0;
            for lines := 0 to size do
            begin
                for i := 0 to spaces do
                    write("");
                for j := 0 to spots do
                    write("*");
                spaces := pred(spaces);	
                spots := succ(spots);
                writeln();	
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Size:')]),CallStmt(Id(r'read'),[Id(r'size')]),Assign(Id(r'spaces'),Id(r'size')),Assign(Id(r'spots'),IntLiteral(0)),For(Id(r'lines'),IntLiteral(0),Id(r'size'),True,[For(Id(r'i'),IntLiteral(0),Id(r'spaces'),True,[CallStmt(Id(r'write'),[StringLiteral(r'')])]),For(Id(r'j'),IntLiteral(0),Id(r'spots'),True,[CallStmt(Id(r'write'),[StringLiteral(r'*')])]),Assign(Id(r'spaces'),CallExpr(Id(r'pred'),[Id(r'spaces')])),Assign(Id(r'spots'),CallExpr(Id(r'succ'),[Id(r'spots')])),CallStmt(Id(r'writeln'),[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 354))
        
    def test_ast_355(self):
        input_prog = """procedure main();
                        begin
            write(":");
            read(amountOfInput);
            sum := 0;
            for i := 1 to amountOfInput do
            begin
                read(number);
                sum := sum + number;
            end
            writeln(sum);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r':')]),CallStmt(Id(r'read'),[Id(r'amountOfInput')]),Assign(Id(r'sum'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),Id(r'amountOfInput'),True,[CallStmt(Id(r'read'),[Id(r'number')]),Assign(Id(r'sum'),BinaryOp('+',Id(r'sum'),Id(r'number')))]),CallStmt(Id(r'writeln'),[Id(r'sum')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 355))
        
    def test_ast_356(self):
        input_prog = """procedure main();
        begin
            read(x, N);
            counter := 0;
            summation := 0;
            while counter <= N do
            begin
                power := 1;
                for i := 0 to counter do
                begin
                    power := power * x;
                end
                summation := summation + power;	
                counter := counter + 1;	
            end
            writeln(summation);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'x'),Id(r'N')]),Assign(Id(r'counter'),IntLiteral(0)),Assign(Id(r'summation'),IntLiteral(0)),While(BinaryOp('<=',Id(r'counter'),Id(r'N')),[Assign(Id(r'power'),IntLiteral(1)),For(Id(r'i'),IntLiteral(0),Id(r'counter'),True,[Assign(Id(r'power'),BinaryOp('*',Id(r'power'),Id(r'x')))]),Assign(Id(r'summation'),BinaryOp('+',Id(r'summation'),Id(r'power'))),Assign(Id(r'counter'),BinaryOp('+',Id(r'counter'),IntLiteral(1)))]),CallStmt(Id(r'writeln'),[Id(r'summation')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 356))
        
    def test_ast_357(self):
        input_prog = """procedure main();
        begin
            while not EOF do begin
                readln(digit);
                writeln("Digitis=", ord(digit));

                if digit > zero then
                    writeln("Predis", pred(digit));

                if digit < nine then
                    writeln("Succis", succ(digit));

            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[While(UnaryOp(r'not',Id(r'EOF')),[CallStmt(Id(r'readln'),[Id(r'digit')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Digitis='),CallExpr(Id(r'ord'),[Id(r'digit')])]),If(BinaryOp('>',Id(r'digit'),Id(r'zero')),[CallStmt(Id(r'writeln'),[StringLiteral(r'Predis'),CallExpr(Id(r'pred'),[Id(r'digit')])])],[]),If(BinaryOp('<',Id(r'digit'),Id(r'nine')),[CallStmt(Id(r'writeln'),[StringLiteral(r'Succis'),CallExpr(Id(r'succ'),[Id(r'digit')])])],[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 357))
        
    def test_ast_358(self):
        input_prog = """procedure main();
        begin

            for i := 1 to 10 do begin
                v[i] := i;
                writeln(v[i], i * i,i * i * i);
            end
            
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Assign(ArrayCell(Id(r'v'),Id(r'i')),Id(r'i')),CallStmt(Id(r'writeln'),[ArrayCell(Id(r'v'),Id(r'i')),BinaryOp('*',Id(r'i'),Id(r'i')),BinaryOp('*',BinaryOp('*',Id(r'i'),Id(r'i')),Id(r'i'))])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 358))
        
    def test_ast_359(self):
        input_prog = """procedure main();
        begin
            size := 0;
            number := 1;
            while number <> 0 do begin
                read(number);
                list[size] := number;
                size := size + 1;
            end
            size := size - 2;

            for i := size downto 0 do
                write(list[i]);
            writeln();
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'size'),IntLiteral(0)),Assign(Id(r'number'),IntLiteral(1)),While(BinaryOp('<>',Id(r'number'),IntLiteral(0)),[CallStmt(Id(r'read'),[Id(r'number')]),Assign(ArrayCell(Id(r'list'),Id(r'size')),Id(r'number')),Assign(Id(r'size'),BinaryOp('+',Id(r'size'),IntLiteral(1)))]),Assign(Id(r'size'),BinaryOp('-',Id(r'size'),IntLiteral(2))),For(Id(r'i'),Id(r'size'),IntLiteral(0),False,[CallStmt(Id(r'write'),[ArrayCell(Id(r'list'),Id(r'i'))])]),CallStmt(Id(r'writeln'),[])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 359))
        
    def test_ast_360(self):
        input_prog = """procedure main();
        begin
            read(real_size);
            if (real_size <= MAX_SIZE) and (real_size > -1) then begin

                for i := 1 to real_size do
                    read(a[i], b[i]);

                writeln();

                for i := 1 to real_size do
                    writeln(a[i], b[i]);		
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'real_size')]),If(BinaryOp('and',BinaryOp('<=',Id(r'real_size'),Id(r'MAX_SIZE')),BinaryOp('>',Id(r'real_size'),UnaryOp(r'-',IntLiteral(1)))),[For(Id(r'i'),IntLiteral(1),Id(r'real_size'),True,[CallStmt(Id(r'read'),[ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'b'),Id(r'i'))])]),CallStmt(Id(r'writeln'),[]),For(Id(r'i'),IntLiteral(1),Id(r'real_size'),True,[CallStmt(Id(r'writeln'),[ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'b'),Id(r'i'))])])],[])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 360))
        
    def test_ast_361(self):
        input_prog = """procedure main();
        begin
            writeln("EnterName");

            for i := 1 to 5 do
                readln(name[i]);

            for i := 1 to 5 do
                writeln(name[i]);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'writeln'),[StringLiteral(r'EnterName')]),For(Id(r'i'),IntLiteral(1),IntLiteral(5),True,[CallStmt(Id(r'readln'),[ArrayCell(Id(r'name'),Id(r'i'))])]),For(Id(r'i'),IntLiteral(1),IntLiteral(5),True,[CallStmt(Id(r'writeln'),[ArrayCell(Id(r'name'),Id(r'i'))])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 361))
        
    def test_ast_362(self):
        input_prog = """procedure main();
        begin
            qbit := 215;
            mit := qbit mod 17;
            qbit := 0;
            while qbit < 245 do
            begin
                writeln(qbit);
                qbit := succ(qbit);
            end

            writeln(qbit);
            writeln(mit);
            {}
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'qbit'),IntLiteral(215)),Assign(Id(r'mit'),BinaryOp('mod',Id(r'qbit'),IntLiteral(17))),Assign(Id(r'qbit'),IntLiteral(0)),While(BinaryOp('<',Id(r'qbit'),IntLiteral(245)),[CallStmt(Id(r'writeln'),[Id(r'qbit')]),Assign(Id(r'qbit'),CallExpr(Id(r'succ'),[Id(r'qbit')]))]),CallStmt(Id(r'writeln'),[Id(r'qbit')]),CallStmt(Id(r'writeln'),[Id(r'mit')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 362))
        
    def test_ast_363(self):
        input_prog = """procedure main();
        begin
            summation := 0.0; current := 0.0;
            for i := 1 to 10 do begin
                read(current);
                v[i] := current;
                summation := summation + current;
            end
            for i := 1 to 9 do
                write(v[i]);
            writeln(v[10] , summation);
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'summation'),FloatLiteral(0.0)),Assign(Id(r'current'),FloatLiteral(0.0)),For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'read'),[Id(r'current')]),Assign(ArrayCell(Id(r'v'),Id(r'i')),Id(r'current')),Assign(Id(r'summation'),BinaryOp('+',Id(r'summation'),Id(r'current')))]),For(Id(r'i'),IntLiteral(1),IntLiteral(9),True,[CallStmt(Id(r'write'),[ArrayCell(Id(r'v'),Id(r'i'))])]),CallStmt(Id(r'writeln'),[ArrayCell(Id(r'v'),IntLiteral(10)),Id(r'summation')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 363))
        
    def test_ast_364(self):
        input_prog = """procedure main();
        begin
            read(wd);
            total := length(wd);
            break;
            writeln(total);
            writeln("LETTER" , "FREQUENCY", "PERCENT" );
            for counter := "a" to "z" do begin
                if freqs[counter] <> 0 then begin
                    percent := (freqs[counter] / total) * 100;
                    writeln(counter,  freqs[counter], percent);
                end
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'wd')]),Assign(Id(r'total'),CallExpr(Id(r'length'),[Id(r'wd')])),Break(),CallStmt(Id(r'writeln'),[Id(r'total')]),CallStmt(Id(r'writeln'),[StringLiteral(r'LETTER'),StringLiteral(r'FREQUENCY'),StringLiteral(r'PERCENT')]),For(Id(r'counter'),StringLiteral(r'a'),StringLiteral(r'z'),True,[If(BinaryOp('<>',ArrayCell(Id(r'freqs'),Id(r'counter')),IntLiteral(0)),[Assign(Id(r'percent'),BinaryOp('*',BinaryOp('/',ArrayCell(Id(r'freqs'),Id(r'counter')),Id(r'total')),IntLiteral(100))),CallStmt(Id(r'writeln'),[Id(r'counter'),ArrayCell(Id(r'freqs'),Id(r'counter')),Id(r'percent')])],[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 364))
        
    def test_ast_365(self):
        input_prog = """
            function ack(m, n : integer) : integer;
            var
            n, m : integer;
            begin
                if m = 0 then ack := n + 1;
                else if (n = 0) and (m > 0) then ack := ack(m - 1, 1);
                else ack := ack(m - 1, ack(m, n - 1));
            end
        procedure main();
        begin
            n := 2; m := 2;
            while n <> 0 do
            begin
                write("m:"); read(m);
                write("n:"); read(n);
                writeln(ack(m, n));
            end
        end"""
        expect = str(Program([FuncDecl(Id(r'ack'),[VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'm'),IntType())],[If(BinaryOp('=',Id(r'm'),IntLiteral(0)),[Assign(Id(r'ack'),BinaryOp('+',Id(r'n'),IntLiteral(1)))],[If(BinaryOp('and',BinaryOp('=',Id(r'n'),IntLiteral(0)),BinaryOp('>',Id(r'm'),IntLiteral(0))),[Assign(Id(r'ack'),CallExpr(Id(r'ack'),[BinaryOp('-',Id(r'm'),IntLiteral(1)),IntLiteral(1)]))],[Assign(Id(r'ack'),CallExpr(Id(r'ack'),[BinaryOp('-',Id(r'm'),IntLiteral(1)),CallExpr(Id(r'ack'),[Id(r'm'),BinaryOp('-',Id(r'n'),IntLiteral(1))])]))])])], IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'n'),IntLiteral(2)),Assign(Id(r'm'),IntLiteral(2)),While(BinaryOp('<>',Id(r'n'),IntLiteral(0)),[CallStmt(Id(r'write'),[StringLiteral(r'm:')]),CallStmt(Id(r'read'),[Id(r'm')]),CallStmt(Id(r'write'),[StringLiteral(r'n:')]),CallStmt(Id(r'read'),[Id(r'n')]),CallStmt(Id(r'writeln'),[CallExpr(Id(r'ack'),[Id(r'm'),Id(r'n')])])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 365))
        
    def test_ast_366(self):
        input_prog = """procedure addrationals(num1, den1 : integer;
                            num2, den2 : integer);
        begin
            num1 := num1 * den2 + num2 * den1;
            den1 := den1 * den2;
        end
        procedure main();
        begin
            read(n1, d1);
            read(n2, d2);
            addrationals(n1, d1, n2, d2);
            writeln(n1, d1);
        end"""
        expect = str(Program([FuncDecl(Id(r'addrationals'),[VarDecl(Id(r'num1'),IntType()),VarDecl(Id(r'den1'),IntType()),VarDecl(Id(r'num2'),IntType()),VarDecl(Id(r'den2'),IntType())],[],[Assign(Id(r'num1'),BinaryOp('+',BinaryOp('*',Id(r'num1'),Id(r'den2')),BinaryOp('*',Id(r'num2'),Id(r'den1')))),Assign(Id(r'den1'),BinaryOp('*',Id(r'den1'),Id(r'den2')))], VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'read'),[Id(r'n1'),Id(r'd1')]),CallStmt(Id(r'read'),[Id(r'n2'),Id(r'd2')]),CallStmt(Id(r'addrationals'),[Id(r'n1'),Id(r'd1'),Id(r'n2'),Id(r'd2')]),CallStmt(Id(r'writeln'),[Id(r'n1'),Id(r'd1')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 366))
        
    def test_ast_367(self):
        input_prog = """procedure change();
        begin
            x := x + 1;	
        end
        procedure main();
        begin
            x := 0;
            writeln(x);
            change();
            writeln(x);
        end"""
        expect = str(Program([FuncDecl(Id(r'change'),[],[],[Assign(Id(r'x'),BinaryOp('+',Id(r'x'),IntLiteral(1)))], VoidType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'x'),IntLiteral(0)),CallStmt(Id(r'writeln'),[Id(r'x')]),CallStmt(Id(r'change'),[]),CallStmt(Id(r'writeln'),[Id(r'x')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 367))
        
    def test_ast_368(self):
        input_prog = """
        procedure change();
        var
            x : integer;
        begin
            x := 1;
        end
        procedure main();
        begin
            x := 0;
            writeln(x);
            change();
            writeln(x);
        end"""
        expect = str(Program([FuncDecl(Id(r'change'),[],[VarDecl(Id(r'x'),IntType())],[Assign(Id(r'x'),IntLiteral(1))], VoidType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'x'),IntLiteral(0)),CallStmt(Id(r'writeln'),[Id(r'x')]),CallStmt(Id(r'change'),[]),CallStmt(Id(r'writeln'),[Id(r'x')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 368))
        
    def test_ast_369(self):
        input_prog = """procedure change(y : integer);
        begin
            y := y + 1;	
        end
        procedure main();
        begin
            (* Cannot call change on an expression, just a variable *)
            x := 0;
            writeln(x);
            change(x);
            writeln(x);
            z := 7;
            writeln(z);
            change(z);
            writeln(z);
        end"""
        expect = str(Program([FuncDecl(Id(r'change'),[VarDecl(Id(r'y'),IntType())],[],[Assign(Id(r'y'),BinaryOp('+',Id(r'y'),IntLiteral(1)))], VoidType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'x'),IntLiteral(0)),CallStmt(Id(r'writeln'),[Id(r'x')]),CallStmt(Id(r'change'),[Id(r'x')]),CallStmt(Id(r'writeln'),[Id(r'x')]),Assign(Id(r'z'),IntLiteral(7)),CallStmt(Id(r'writeln'),[Id(r'z')]),CallStmt(Id(r'change'),[Id(r'z')]),CallStmt(Id(r'writeln'),[Id(r'z')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 369))
        
    def test_ast_370(self):
        input_prog = """procedure change(y : integer);
        begin
            y := 1;	
        end
        procedure main();
        begin
            x := 0;
            writeln(x);
            change(x);
            writeln(x);
            change(2 + 5); (* Allows expressions *)
        end"""
        expect = str(Program([FuncDecl(Id(r'change'),[VarDecl(Id(r'y'),IntType())],[],[Assign(Id(r'y'),IntLiteral(1))], VoidType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'x'),IntLiteral(0)),CallStmt(Id(r'writeln'),[Id(r'x')]),CallStmt(Id(r'change'),[Id(r'x')]),CallStmt(Id(r'writeln'),[Id(r'x')]),CallStmt(Id(r'change'),[BinaryOp('+',IntLiteral(2),IntLiteral(5))])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 370))
        
    def test_ast_371(self):
        input_prog = """procedure triangle(bound : integer);
                var i, j : integer;
            begin
                i := 0;
                while i <= bound do begin
                    j := 0; 
                    while j <= i do begin
                        write(pascal(i, j));
                        j := j + 1;
                    end
                    i := i + 1; 
                    writeln();
                end
            end"""
        expect = str(Program([FuncDecl(Id(r'triangle'),[VarDecl(Id(r'bound'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType())],[Assign(Id(r'i'),IntLiteral(0)),While(BinaryOp('<=',Id(r'i'),Id(r'bound')),[Assign(Id(r'j'),IntLiteral(0)),While(BinaryOp('<=',Id(r'j'),Id(r'i')),[CallStmt(Id(r'write'),[CallExpr(Id(r'pascal'),[Id(r'i'),Id(r'j')])]),Assign(Id(r'j'),BinaryOp('+',Id(r'j'),IntLiteral(1)))]),Assign(Id(r'i'),BinaryOp('+',Id(r'i'),IntLiteral(1))),CallStmt(Id(r'writeln'),[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 371))
        
    def test_ast_372(self):
        input_prog = """function pascal(r, c : integer) : integer;

            begin
                if (c = 0) or (c = r) then
                    pascal := 1;
                else
                    pascal := pascal(r - 1, c - 1) + pascal(r - 1, c) ;
            end"""
        expect = str(Program([FuncDecl(Id(r'pascal'),[VarDecl(Id(r'r'),IntType()),VarDecl(Id(r'c'),IntType())],[],[If(BinaryOp('or',BinaryOp('=',Id(r'c'),IntLiteral(0)),BinaryOp('=',Id(r'c'),Id(r'r'))),[Assign(Id(r'pascal'),IntLiteral(1))],[Assign(Id(r'pascal'),BinaryOp('+',CallExpr(Id(r'pascal'),[BinaryOp('-',Id(r'r'),IntLiteral(1)),BinaryOp('-',Id(r'c'),IntLiteral(1))]),CallExpr(Id(r'pascal'),[BinaryOp('-',Id(r'r'),IntLiteral(1)),Id(r'c')])))])], IntType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 372))
        
    def test_ast_373(self):
        input_prog = """var n : integer;
        function power2(n:integer): integer;
        var k : integer;
        begin
            k := 0;
            while (n mod 2 = 0) do
            begin
                k := succ(k);
                n := n div 2;
            end
            power2 := k;
        end"""
        expect = str(Program([VarDecl(Id(r'n'),IntType()),FuncDecl(Id(r'power2'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'k'),IntType())],[Assign(Id(r'k'),IntLiteral(0)),While(BinaryOp('=',BinaryOp('mod',Id(r'n'),IntLiteral(2)),IntLiteral(0)),[Assign(Id(r'k'),CallExpr(Id(r'succ'),[Id(r'k')])),Assign(Id(r'n'),BinaryOp('div',Id(r'n'),IntLiteral(2)))]),Assign(Id(r'power2'),Id(r'k'))], IntType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 373))
        
    def test_ast_374(self):
        input_prog = """function isPrime(n : integer) : boolean;
            var
                soFarPrime : boolean;
                candidate : integer;

            begin
                soFarPrime := TRUE;

                for candidate := 2 to (n - 1) do
                    if (n mod candidate = 0) then
                        soFarPrime := FALSE;
                isPrime := soFarPrime;
            end"""
        expect = str(Program([FuncDecl(Id(r'isPrime'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'soFarPrime'),BoolType()),VarDecl(Id(r'candidate'),IntType())],[Assign(Id(r'soFarPrime'),BooleanLiteral(True)),For(Id(r'candidate'),IntLiteral(2),BinaryOp('-',Id(r'n'),IntLiteral(1)),True,[If(BinaryOp('=',BinaryOp('mod',Id(r'n'),Id(r'candidate')),IntLiteral(0)),[Assign(Id(r'soFarPrime'),BooleanLiteral(False))],[])]),Assign(Id(r'isPrime'),Id(r'soFarPrime'))], BoolType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 374))
        
    def test_ast_375(self):
        input_prog = """procedure printPrimesUpTo(bound : integer);
            var
                i : integer;
            begin 
                for i := 1 to bound do
                    if isPrime(i) then write(i);
            end
        """
        expect = str(Program([FuncDecl(Id(r'printPrimesUpTo'),[VarDecl(Id(r'bound'),IntType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(1),Id(r'bound'),True,[If(CallExpr(Id(r'isPrime'),[Id(r'i')]),[CallStmt(Id(r'write'),[Id(r'i')])],[])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 375))
        
    def test_ast_376(self):
        input_prog = """procedure main();
        begin
        a := - "xy";
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),UnaryOp(r'-',StringLiteral(r'xy')))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 376))
        
    def test_ast_377(self):
        input_prog = """procedure main();
        var a, id: integer;
        begin
        
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'id'),IntType())],[], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 377))
        
    def test_ast_378(self):
        input_prog = """procedure main();
        begin
        a := b[10] := foo ()[3] := x := 1 ;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'x'),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3)),Id(r'x')),Assign(ArrayCell(Id(r'b'),IntLiteral(10)),ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3))),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(10)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 378))
        
    def test_ast_379(self):
        input_prog = """procedure main();
        begin
        a := -- 9;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),UnaryOp(r'-',UnaryOp(r'-',IntLiteral(9))))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 379))
        
    def test_ast_380(self):
        input_prog = """
        procedure TPascalMinerAppOnInThreadNewLog(logtype: Real; Time: Real;
        ThreadID: Real; sender, logtext: Real);
        var msg : String;
        i,nline : Integer;
        begin
        If logtype=ltdebug then break;
        break;  
        end

        """
        expect = str(Program([FuncDecl(Id(r'TPascalMinerAppOnInThreadNewLog'),[VarDecl(Id(r'logtype'),FloatType()),VarDecl(Id(r'Time'),FloatType()),VarDecl(Id(r'ThreadID'),FloatType()),VarDecl(Id(r'sender'),FloatType()),VarDecl(Id(r'logtext'),FloatType())],[VarDecl(Id(r'msg'),StringType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'nline'),IntType())],[If(BinaryOp('=',Id(r'logtype'),Id(r'ltdebug')),[Break()],[]),Break()], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 380))
        
    def test_ast_381(self):
        input_prog = """procedure TPascalMinerAppShowGPUDrivers();
        Var i,j,n : Integer;
        x, y, z: real;
        x, y, z: real;
        x, y, z: real;
        x, y, z: real;
        begin
        n := 0;
        If Not TGPUDriverGPUDriverHasOpenCL then WriteLn("54");
        else 
        begin
            Writeln("");
            
            for i:=0 to TGPUDriverGPUDriverPlatformsPlatformCount-1 do begin
            for j:=0 to TGPUDriverGPUDriverPlatformsPlatforms[i]*DeviceCount-1 do begin
                dev := TGPUDriverGPUDriverPlatformsPlatforms[i]*Devices[j];
                
            end
            end
        end
        end"""
        expect = str(Program([FuncDecl(Id(r'TPascalMinerAppShowGPUDrivers'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType())],[Assign(Id(r'n'),IntLiteral(0)),If(UnaryOp(r'Not',Id(r'TGPUDriverGPUDriverHasOpenCL')),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'54')])],[CallStmt(Id(r'Writeln'),[StringLiteral(r'')]),For(Id(r'i'),IntLiteral(0),BinaryOp('-',Id(r'TGPUDriverGPUDriverPlatformsPlatformCount'),IntLiteral(1)),True,[For(Id(r'j'),IntLiteral(0),BinaryOp('-',BinaryOp('*',ArrayCell(Id(r'TGPUDriverGPUDriverPlatformsPlatforms'),Id(r'i')),Id(r'DeviceCount')),IntLiteral(1)),True,[Assign(Id(r'dev'),BinaryOp('*',ArrayCell(Id(r'TGPUDriverGPUDriverPlatformsPlatforms'),Id(r'i')),ArrayCell(Id(r'Devices'),Id(r'j'))))])])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 381))
        
    def test_ast_382(self):
        input_prog = """var i, x, z, g, y : array [1 .. 5] of integer ;
        var i : array [1 .. 5] of real ;
        var i : array [1 .. 5] of string ;
        var i : array [1 .. 5] of boolean ;"""
        expect = str(Program([VarDecl(Id(r'i'),ArrayType(1,5,IntType())),VarDecl(Id(r'x'),ArrayType(1,5,IntType())),VarDecl(Id(r'z'),ArrayType(1,5,IntType())),VarDecl(Id(r'g'),ArrayType(1,5,IntType())),VarDecl(Id(r'y'),ArrayType(1,5,IntType())),VarDecl(Id(r'i'),ArrayType(1,5,FloatType())),VarDecl(Id(r'i'),ArrayType(1,5,StringType())),VarDecl(Id(r'i'),ArrayType(1,5,BoolType()))]))
        self.assertTrue(TestAST.test(input_prog, expect, 382))
        
    def test_ast_383(self):
        input_prog = """var a , b , c : integer ;
        d : array [ 1 .. 5 ] of integer ;
        e , f : real ;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),ArrayType(1,5,IntType())),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),FloatType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 383))
        
    def test_ast_384(self):
        input_prog = """function foo ( a , b : integer ; c : real ) : array [1 .. 2] of integer ;
        var x , y : real;
        begin
        end"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[], ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input_prog, expect, 384))
        
    def test_ast_385(self):
        input_prog = """procedure foo ( a , b : integer ; c : real ) ;
        var x,y: real;
        begin (* This is
        a block comment *)
        end { This is a block comment } // This is also a comment"""
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 385))
        
    def test_ast_386(self):
        input_prog = """procedure main();
        begin
        a := 1.2;
        b := 1.;
        c := .1;
        d := 1e2;
        e := 1.2E-2;
        f := 1.2e-2;
        g := .1E2;
        h := 9.0;
        i := 12e8;
        j := 0.33E-3;
        k := 128e-42;
        end
        """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),FloatLiteral(1.2)),Assign(Id(r'b'),FloatLiteral(1.0)),Assign(Id(r'c'),FloatLiteral(0.1)),Assign(Id(r'd'),FloatLiteral(100.0)),Assign(Id(r'e'),FloatLiteral(0.012)),Assign(Id(r'f'),FloatLiteral(0.012)),Assign(Id(r'g'),FloatLiteral(10.0)),Assign(Id(r'h'),FloatLiteral(9.0)),Assign(Id(r'i'),FloatLiteral(1200000000.0)),Assign(Id(r'j'),FloatLiteral(0.00033)),Assign(Id(r'k'),FloatLiteral(1.28e-40))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 386))
        
    def test_ast_387(self):
        input_prog = """procedure main();
        begin
        foo(2)[3+x] := a[b[2]] +3;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral(3),Id(r'x'))),BinaryOp('+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(3)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 387))
        
    def test_ast_388(self):
        input_prog = """procedure goo ( x : array [ 1 .. 2 ] of real ) ;
        var
        y : array [ 2 .. 3 ] of real ;
        z : array [ 1 .. 2 ] of integer ;
        begin
            foo ( x ) ; //CORRECT
            foo ( y ) ; //WRONG
            foo ( z ) ; //WRONG
        end"""
        expect = str(Program([FuncDecl(Id(r'goo'),[VarDecl(Id(r'x'),ArrayType(1,2,FloatType()))],[VarDecl(Id(r'y'),ArrayType(2,3,FloatType())),VarDecl(Id(r'z'),ArrayType(1,2,IntType()))],[CallStmt(Id(r'foo'),[Id(r'x')]),CallStmt(Id(r'foo'),[Id(r'y')]),CallStmt(Id(r'foo'),[Id(r'z')])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 388))
        
    def test_ast_389(self):
        input_prog = """procedure main();
        begin
        a := b [10] := foo ( ) [3] := x := 1 ;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'x'),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3)),Id(r'x')),Assign(ArrayCell(Id(r'b'),IntLiteral(10)),ArrayCell(CallExpr(Id(r'foo'),[]),IntLiteral(3))),Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(10)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 389))
        
    def test_ast_390(self):
        input_prog = """
        procedure main();
        begin
        if a then
        b := 100;


        if c then 
            b := 100;
        else
            c := 100;
            end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(Id(r'a'),[Assign(Id(r'b'),IntLiteral(100))],[]),If(Id(r'c'),[Assign(Id(r'b'),IntLiteral(100))],[Assign(Id(r'c'),IntLiteral(100))])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 390))
        
    def test_ast_391(self):
        input_prog = """procedure main();
        begin
        with a , b : integer ; c : array [ 1 .. 2 ] of real ; do
            d := c[a] + b;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp('+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b')))])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 391))
        
    def test_ast_392(self):
        input_prog = """procedure main();
        begin
        foo ( 3 , a+1, m( 2 ) ) ;
        end
        """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'foo'),[IntLiteral(3),BinaryOp('+',Id(r'a'),IntLiteral(1)),CallExpr(Id(r'm'),[IntLiteral(2)])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 392))
        
    def test_ast_393(self):
        input_prog = """var i : integer ;
        function f ( ) : integer ;
        begin
            return 200;
        end
        procedure main ( );
        var
            main: integer;
        begin
            main := f();
            putIntLn ( main ) ;
            with i : integer ;main : integer ;f : integer ; do
            begin
                main := f := i := 100;
                putIntLn ( i ) ;
                putIntLn ( main ) ;
                putIntLn ( f ) ;
            end
            putIntLn ( main ) ;
        end
        var g:real;"""
        expect = str(Program([VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'f'),[],[],[Return(IntLiteral(200))], IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'main'),IntType())],[Assign(Id(r'main'),CallExpr(Id(r'f'),[])),CallStmt(Id(r'putIntLn'),[Id(r'main')]),With([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'main'),IntType()),VarDecl(Id(r'f'),IntType())],[Assign(Id(r'i'),IntLiteral(100)),Assign(Id(r'f'),Id(r'i')),Assign(Id(r'main'),Id(r'f')),CallStmt(Id(r'putIntLn'),[Id(r'i')]),CallStmt(Id(r'putIntLn'),[Id(r'main')]),CallStmt(Id(r'putIntLn'),[Id(r'f')])]),CallStmt(Id(r'putIntLn'),[Id(r'main')])], VoidType()),VarDecl(Id(r'g'),FloatType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 393))
        
    def test_ast_394(self):
        input_prog = """
        procedure main();
        begin
        a := -7;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),UnaryOp(r'-',IntLiteral(7)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 394))
        
    def test_ast_395(self):
        input_prog = """procedure main();
        begin
        a := -a[-9] + - foo();
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),BinaryOp('+',UnaryOp(r'-',ArrayCell(Id(r'a'),UnaryOp(r'-',IntLiteral(9)))),UnaryOp(r'-',CallExpr(Id(r'foo'),[]))))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 395))
        
    def test_ast_396(self):
        input_prog = """procedure main();
        begin
        foo(-2)[-3+x] := a[b[2]] +3;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(ArrayCell(CallExpr(Id(r'foo'),[UnaryOp(r'-',IntLiteral(2))]),BinaryOp('+',UnaryOp(r'-',IntLiteral(3)),Id(r'x'))),BinaryOp('+',ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),IntLiteral(3)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 396))
        
    def test_ast_397(self):
        input_prog = """procedure main();
        begin
        a := "asdasdasd asdasd";
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),StringLiteral(r'asdasdasd asdasd'))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 397))
        
    def test_ast_398(self):
        input_prog = """procedure main();
        begin
        a := 10 + b * 99 / 33 - jd + 89 - - - - - - - - - - - - - - - - - - - - - - - - - - 79 + jdi div asd;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),BinaryOp('+',BinaryOp('-',BinaryOp('+',BinaryOp('-',BinaryOp('+',IntLiteral(10),BinaryOp('/',BinaryOp('*',Id(r'b'),IntLiteral(99)),IntLiteral(33))),Id(r'jd')),IntLiteral(89)),UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',UnaryOp(r'-',IntLiteral(79))))))))))))))))))))))))))),BinaryOp('div',Id(r'jdi'),Id(r'asd'))))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 398))
        
    def test_ast_399(self):
        input_prog = """procedure main();
        begin
        with a , b, d, e, f : integer ; c : array [ 1 .. 2 ] of real; do
        d := c [ a ] + b ;
        break;
        continue;
        call(thisGuy, thisOtherGuy, thisFunc(asdas, ahsdasd));
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'e'),IntType()),VarDecl(Id(r'f'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'd'),BinaryOp('+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b')))]),Break(),Continue(),CallStmt(Id(r'call'),[Id(r'thisGuy'),Id(r'thisOtherGuy'),CallExpr(Id(r'thisFunc'),[Id(r'asdas'),Id(r'ahsdasd')])])], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 399))
        
    def test_ast_400(self):
        input_prog = """procedure main();
        begin
        -e := a - 3;
        end"""
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(UnaryOp(r'-',Id(r'e')),BinaryOp('-',Id(r'a'),IntLiteral(3)))], VoidType())]))
        self.assertTrue(TestAST.test(input_prog, expect, 400))
        