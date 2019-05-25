import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    expect = "successful"

    def test_program_1(self):
        
        self.assertTrue(TestParser.test("""
        procedure main();
        begin
        foo(2)[3+x] := a[b[2]] +3;
        end""", self.expect,101))

    def test_program_2(self):
        self.assertTrue(TestParser.test("""
        procedure main();
        begin
        call(1, call2("xyz", 3 + 5 - not 4 or 3 / 1.3e99 * 1.5, true, false),
        calle(a[17], true + false, a["sai"]));
        end""",self.expect,102))
    def test_program_3(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        call();
        end""",self.expect,103))
    def test_program_5(self):
        self.assertTrue(TestParser.test("""procedure _main(a5: integer; hihi: array [1 .. 5] of integer);
        begin
            a := "quyxyha";
        end 
        function _main(a5: integer; concu: array [1 .. 5] of integer): real;
        begin
            a := "quyxyha";
            b := true;
        end""",self.expect,105))
    def test_program_6(self):
        self.assertTrue(TestParser.test("""function _main(a5: integer; concu: array [1 .. 5] of integer): integer;
            begin
                a := "quyxyha";
                b := true;
            end""",self.expect,106))
    def test_program_7(self):
        self.assertTrue(TestParser.test("""function _main(a5: integer; concu: array [1 .. 5] of integer): integer;
            begin
                a := "quyxyha";
                b := true;
                break;
                continue;
                return abc;
            end""",self.expect,107))
    def test_program_8(self):
        self.assertTrue(TestParser.test("""function _main(a5: integer; concu: array [1 .. 5] of integer): array [99 .. 88] of integer;
            begin
                a := "quyxyha";
                b := true;
                break;
                continue;
                return abc;
            end""",self.expect,108))
    def test_program_9(self):
        self.assertTrue(TestParser.test("""var i : integer ;
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
            var g : real ;""",self.expect,109))
    def test_program_10(self):
        self.assertTrue(TestParser.test("""procedure main();
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
            end""",self.expect,110))
    def test_program_11(self):
        self.assertTrue(TestParser.test("""
        procedure main();
        Begin
            Write("HelloWorld.PreparetolearnPASCAL!!");
        End""",self.expect,111))
    def test_program_12(self):
        self.assertTrue(TestParser.test("""
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
        end""",self.expect,112))
    def test_program_13(self):
        self.assertTrue(TestParser.test("""
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
        """,self.expect,113))
    def test_program_14(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        if ReturnCode <> OK then
            {*   Write(SayCalRe(ReturnCode));
            Writeln("");                   *}
                Msg1(Output,1, addr(SayCalRe(ReturnCode)) );
            else Msg0(Output, 2);
        end""",self.expect,114))
    def test_program_15(self):
        self.assertTrue(TestParser.test("""
        procedure main();
        begin
        x := not abc(GetIPAddr(Trim(Ltrim(Line)), HostAddress,
                     AddrSpec, Lookup));
        end""",self.expect,115))
    def test_program_16(self):
        self.assertTrue(TestParser.test("""
        procedure main();
        begin
        with a ,b: integer ; c : array [ 1 .. 2 ] of real ; do
            d := c[a] + b;
        end""",self.expect,116))
    def test_program_17(self):
        self.assertTrue(TestParser.test("""function foo (): real ;
            begin
                if a then return 2.3; // CORRECT
                else return 2; // CORRECT
            end""",self.expect,117))
    def test_program_18(self):
        self.assertTrue(TestParser.test("""function foo (b: array [ 1 .. 2 ] of integer ): array [2 .. 3] of real ;
            var
            a : array [2 .. 3] of real ;
            begin
            if (a) then return a ; //CORRECT
            else return b; //WRONG
            end""",self.expect,118))
    def test_program_19(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        foo(2)[3+x] := a[b[2]] +3; (* ahsdiuahsidh *)
        end""",self.expect,119))
    def test_program_20(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        a := - true; // aHihi
            b := - 15; (* how about this *)
            b := - 15;
        end { so this }""",self.expect,120))
    def test_program_21(self):
        self.assertTrue(TestParser.test("""
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
	end""",self.expect,121))

    def test_program_22(self):
        self.assertTrue(TestParser.test("""
        procedure main();
        var
            charcount, blankcount, commacount, periodcount: integer;
            character : real;
        begin
            
            
        end""",self.expect,122))

    def test_program_23(self):
        self.assertTrue(TestParser.test("""
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
        end""",self.expect,123))

    def test_program_24(self):
        self.assertTrue(TestParser.test("""
        procedure main();
        var
            inches, cent: Real;
        (* This is a comment *)
        begin
            write("Enteralengthininches:");
            readln(inches);
            cent := CENT_PER_INCH * inches;
        end""",self.expect,124))

    def test_program_25(self):
        self.assertTrue(TestParser.test("""procedure main();
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
                        end""",self.expect,125))

    def test_program_26(self):
        self.assertTrue(TestParser.test("""procedure main();
                        begin
                    for base := 1 to tableSize do
                    begin
                        square := sqr(base);
                        cube := base * square;
                        quad := sqr(square);
                        writeln(base, square, cube, quad, 1/base, 1/square,
                            1/cube, 1/quad);
                                
                    end
                    end""",self.expect,126))

    def test_program_27(self):
        self.assertTrue(TestParser.test("""
        procedure main();
                        begin
                        write("Enteranumber:" );
                    read(x);
                    if x >= 0
                        then writeln(sqrt(x));
                        else writeln(x, "Doesnothavearealsquareroot.");	
                    end""",self.expect,127))

    def test_program_28(self):
        self.assertTrue(TestParser.test("""procedure who(input: real; output: Integer);
        var
            name: array [1 .. 20] of real;
            letter: Integer;
        begin
            write("Whatsyourname?:");
            for letter := 1 to 20 do 
                read(name[letter]);
            writeln(name);
        end""",self.expect,128))

    def test_program_29(self):
        self.assertTrue(TestParser.test("""function assignments(output: real):real ;
        var
            period: real;
            gravitational_force : real;

        begin
            period := 2 * pi * sqrt(15/9.81);
            gravitational_force := (6.673E-8 * 34 * 65) / sqr(9);
            writeln(gravitational_force);
        end""",self.expect,129))

    def test_program_30(self):
        self.assertTrue(TestParser.test("""procedure expressions();
        {}
        begin
            writeln(pred(5), succ(5));
            writeln(pred(5), abs(-4));
            writeln(pred(5), sqr(-4));
            writeln(sin(pi), sqr(-4));
            writeln(succ("a"));
        end""",self.expect,130))

    def test_program_31(self):
        self.assertTrue(TestParser.test("""procedure pas();
        var
            x : integer;
        begin
            write(":");
            read(x);
            if x < 0 then 
                x := -x;
            writeln(x);	
        end""",self.expect,131))

    def test_program_32(self):
        self.assertTrue(TestParser.test("""procedure average();
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
        end""",self.expect,132))

    def test_program_33(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,133))

    def test_program_34(self):
        self.assertTrue(TestParser.test("""
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
        end""",self.expect,134))

    def test_program_35(self):
        self.assertTrue(TestParser.test("""procedure main();
                        begin
            writeln("Countdownhasbegun");
            sec := 10;
                sec := sec - 1;	
            writeln("Zero");
        end""",self.expect,135))

    def test_program_36(self):
        self.assertTrue(TestParser.test("""procedure main();
                        begin
            write("n:");
            read(number);
            for i := 0 to number do
                if (i mod 2 = 0) then
                    write(i, "");
            writeln();
        end""",self.expect,136))

    def test_program_37(self):
        self.assertTrue(TestParser.test("""procedure main();
                    
                        begin
            read(number);
            fact := 1;
            for i := number downto 1 do
            begin
                fact := fact * i;		
            end
            writeln(fact);
            {}
        end""",self.expect,137))

    def test_program_38(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,138))

    def test_program_39(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,139))

    def test_program_40(self):
        self.assertTrue(TestParser.test("""procedure main();
                        begin
            termcount := 0;
            sum := 0;
            read(limit);
                termcount := succ(termcount);
                sum := sum + (1 / termcount);		
        end""",self.expect,140))

    def test_program_41(self):
        self.assertTrue(TestParser.test("""procedure main();
                        begin
            summation := 0;
            variable := 0;
            while(summation <= BOUND) do
            begin
                summation := summation + variable * variable * variable;
                variable := succ(variable);		
            end
            writeln(variable);
        end""",self.expect,141))

    def test_program_42(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,142))

    def test_program_43(self):
        self.assertTrue(TestParser.test("""procedure main();
                        begin
            read(number);
            counter := 1;
            while (counter <> MAX) do
            begin
                writeln(number, "*", counter, "=", number * counter);
                counter := succ(counter);
            end
        end""",self.expect,143))

    def test_program_44(self):
        self.assertTrue(TestParser.test("""procedure main();
                        begin
            write("n:");
            read(number);
            for i := 0 to number do
                if (i mod 2 <> 0) then
                    write(i);
            writeln();
        end""",self.expect,144))
    
    def test_program_45(self):
        self.assertTrue(TestParser.test("""procedure main();
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
            end""",self.expect,145))

    def test_program_46(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,146))

    def test_program_47(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,147))

    def test_program_48(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,148))

    def test_program_49(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,149))

    def test_program_50(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,150))

    def test_program_51(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,151))

    def test_program_52(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,152))

    def test_program_53(self):
        self.assertTrue(TestParser.test("""procedure main();
                        begin
            for n := 1 to (maxint - 1) do
            begin
                left := 1 / (n + 1);
                center := ln((n + 1) / n);
                rigth := 1 / n;
                writeln(n, (left < center)  and (center < rigth));		
            end
        end""",self.expect,153))

    def test_program_54(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,154))

    def test_program_55(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,155))

    def test_program_56(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,156))

    def test_program_57(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
            while not EOF do begin
                readln(digit);
                writeln("Digitis=", ord(digit));

                if digit > zero then
                    writeln("Predis", pred(digit));

                if digit < nine then
                    writeln("Succis", succ(digit));

            end
        end""",self.expect,157))

    def test_program_58(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin

            for i := 1 to 10 do begin
                v[i] := i;
                writeln(v[i], i * i,i * i * i);
            end
            
        end""",self.expect,158))

    def test_program_59(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,159))

    def test_program_60(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
            read(real_size);
            if (real_size <= MAX_SIZE) and (real_size > -1) then begin

                for i := 1 to real_size do
                    read(a[i], b[i]);

                writeln();

                for i := 1 to real_size do
                    writeln(a[i], b[i]);		
            end
        end""",self.expect,160))

    def test_program_61(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
            writeln("EnterName");

            for i := 1 to 5 do
                readln(name[i]);

            for i := 1 to 5 do
                writeln(name[i]);
        end""",self.expect,161))

    def test_program_62(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,162))

    def test_program_63(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,163))

    def test_program_64(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        end""",self.expect,164))

    def test_program_65(self):
        self.assertTrue(TestParser.test("""
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
        end""",self.expect,165))

    def test_program_66(self):
        self.assertTrue(TestParser.test("""procedure addrationals(num1, den1 : integer;
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
        end""",self.expect,166))

    def test_program_67(self):
        self.assertTrue(TestParser.test("""procedure change();
        begin
            x := x + 1;	
        end
        procedure main();
        begin
            x := 0;
            writeln(x);
            change();
            writeln(x);
        end""",self.expect,167))

    def test_program_68(self):
        self.assertTrue(TestParser.test("""
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
        end""",self.expect,168))

    def test_program_69(self):
        self.assertTrue(TestParser.test("""procedure change(y : integer);
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
        end""",self.expect,169))

    def test_program_70(self):
        self.assertTrue(TestParser.test("""procedure change(y : integer);
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
        end""",self.expect,170))

    def test_program_71(self):
        self.assertTrue(TestParser.test("""procedure triangle(bound : integer);
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
            end""",self.expect,171))

    def test_program_72(self):
        self.assertTrue(TestParser.test("""function pascal(r, c : integer) : integer;

            begin
                if (c = 0) or (c = r) then
                    pascal := 1
                else
                    pascal := pascal(r - 1, c - 1) + pascal(r - 1, c) ;
            end""",self.expect,172))

    def test_program_73(self):
        self.assertTrue(TestParser.test("""var n : integer;
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
        end""",self.expect,173))

    def test_program_74(self):
        self.assertTrue(TestParser.test("""function isPrime(n : integer) : boolean;
            var
                soFarPrime : boolean;
                candidate : integer;

            begin
                soFarPrime := TRUE;

                for candidate := 2 to (n - 1) do
                    if (n mod candidate = 0) then
                        soFarPrime := FALSE;
                isPrime := soFarPrime;
            end""",self.expect,174))

    def test_program_75(self):
        self.assertTrue(TestParser.test("""procedure printPrimesUpTo(bound : integer);
            var
                i : integer;
            begin 
                for i := 1 to bound do
                    if isPrime(i) then write(i);
            end
        """,self.expect,175))

    def test_program_76(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        a := - "xy";
        end""",self.expect,176))

    def test_program_77(self):
        self.assertTrue(TestParser.test("""procedure main();
        var a, id: integer;
        begin
        
        end""",self.expect,177))

    def test_program_78(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        a := b[10] := foo ()[3] := x := 1 ;
        end""",self.expect,178))

    def test_program_79(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        a := -- 9;
        end""",self.expect,179))

    def test_program_80(self):
        self.assertTrue(TestParser.test("""
        procedure TPascalMinerAppOnInThreadNewLog(logtype: Real; Time: Real;
        ThreadID: Real; sender, logtext: Real);
        var msg : String;
        i,nline : Integer;
        begin
        If logtype=ltdebug then break;
        break;  
        end

        """,self.expect,180))

    def test_program_81(self):
        self.assertTrue(TestParser.test("""procedure TPascalMinerAppShowGPUDrivers();
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
        end""",self.expect,181))

    def test_program_82(self):
        self.assertTrue(TestParser.test("""var i, x, z, g, y : array [1 .. 5] of integer ;
        var i : array [1 .. 5] of real ;
        var i : array [1 .. 5] of string ;
        var i : array [1 .. 5] of boolean ;""",self.expect,182))

    def test_program_83(self):
        self.assertTrue(TestParser.test("""var a , b , c : integer ;
        d : array [ 1 .. 5 ] of integer ;
        e , f : real ;""",self.expect,183))

    def test_program_84(self):
        self.assertTrue(TestParser.test("""function foo ( a , b : integer ; c : real ) : array [1 .. 2] of integer ;
        var x , y : real;
        begin
        end""",self.expect,184))

    def test_program_85(self):
        self.assertTrue(TestParser.test("""procedure foo ( a , b : integer ; c : real ) ;
        var x,y: real;
        begin (* This is
        a block comment *)
        end { This is a block comment } // This is also a comment""",self.expect,185))

    def test_program_86(self):
        self.assertTrue(TestParser.test("""procedure main();
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
        """,self.expect,186))

    def test_program_87(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        foo(2)[3+x] := a[b[2]] +3;
        end""",self.expect,187))

    def test_program_88(self):
        self.assertTrue(TestParser.test("""procedure goo ( x : array [ 1 .. 2 ] of real ) ;
        var
        y : array [ 2 .. 3 ] of real ;
        z : array [ 1 .. 2 ] of integer ;
        begin
            foo ( x ) ; //CORRECT
            foo ( y ) ; //WRONG
            foo ( z ) ; //WRONG
        end""",self.expect,188))

    def test_program_89(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        a := b [10] := foo ( ) [3] := x := 1 ;
        end""",self.expect,189))

    def test_program_90(self):
        self.assertTrue(TestParser.test("""
        procedure main();
        begin
        if a then
        b := 100;


        if c then 
            b := 100;
        else
            c := 100;
            end""",self.expect,190))

    def test_program_91(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        with a , b : integer ; c : array [ 1 .. 2 ] of real ; do
            d := c[a] + b;
        end""",self.expect,191))

    def test_program_92(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        foo ( 3 , a+1, m( 2 ) ) ;
        end
        """,self.expect,192))

    def test_program_93(self):
        self.assertTrue(TestParser.test("""var i : integer ;
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
        var g:real;""",self.expect,193))

    def test_program_94(self):
        self.assertTrue(TestParser.test("""
        procedure main();
        begin
        a := -7;
        end""",self.expect,194))

    def test_program_95(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        a := -a[-9] + - foo();
        end""",self.expect,195))

    def test_program_96(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        foo(-2)[-3+x] := a[b[2]] +3;
        end""",self.expect,196))

    def test_program_97(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        a := "asdasdasd asdasd";
        end""",self.expect,197))

    def test_program_98(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        a := 10 + b * 99 / 33 - jd + 89 - - - - - - - - - - - - - - - - - - - - - - - - - - 79 + jdi div asd;
        end""",self.expect,198))

    def test_program_99(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        with a , b, d, e, f : integer ; c : array [ 1 .. 2 ] of real; do
        d := c [ a ] + b ;
        break;
        continue;
        call(thisGuy, thisOtherGuy, thisFunc(asdas, ahsdasd));
        end""",self.expect,199))

    def test_program_100(self):
        self.assertTrue(TestParser.test("""procedure main();
        begin
        -e := a - 3;
        end""",self.expect,200))



        

        

        
        

    