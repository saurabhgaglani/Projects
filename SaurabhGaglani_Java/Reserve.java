
import java.io.*;
public class Reserve
{
 public static void func3() throws IOException
 {
  BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
  System.out.println('\f');
  Railway.headingLine();
  Railway.blankLines(1);
  System.out.println("\t\t\t\t RESERVATION CHART");
  Railway.headingLine();
  Railway.blankLines(1);
  int flag4=0,i4=0,tno=0;
  while (flag4==0)
  {
  System.out.print("Please enter the train number :");
  tno = Integer.parseInt(br.readLine());
  for (i4=0; i4<=1; i4++)
   {if (Railway.trno[i4]== tno)
    {flag4=1;
     break;
    }
   }
  if (flag4==0)
   continue;
  }
  int ctr4=1;
  String max2="";
  while (ctr4<=3)
  {
   if (i4==0 && ctr4==1)
   { System.out.println("CLASS AC :");
     max2= "AC";}
   if (i4==0 & ctr4==2)
   { System.out.println("FIRST CLASS :");
      max2="First";} 
   if (i4==0 && ctr4==3)
    {System.out.println("SECOND CLASS :");
     max2="Second";}
   if (i4==1 && ctr4==1)
   { System.out.println("CLASS AC :");
       max2="AC";}
   if (i4==1 && ctr4==2)
    {System.out.println("FIRST CLASS :");   
     max2="First";}
   if (i4==1 && ctr4==3)
    {System.out.println("SECOND CLASS :");   
     max2="Second";}
   System.out.println("prno.   train No.   Name     \tTotal seats      class"); 
   for (int pm=0; pm<25; pm++)
   { if (Railway.prno[pm]!=0 && Railway.trnum[pm]==tno && (Railway.clas[pm].equals(max2)))
       System.out.println(Railway.prno[pm]+"\t "+Railway.trnum[pm]+"\t   "+ Railway.bookperson[pm]+"\t\t"+"("+Railway.setno[pm]+") "+Railway.seat[pm]+"\t  "+Railway.clas[pm]);
   }
   ctr4= ctr4+1;
   Railway.blankLines(1);
  }
  Railway.pressKey();
 }
 
 public static void func5() throws IOException 
 {
  BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
  System.out.println('\f');
  Railway.headingLine();
  System.out.println();
  System.out.println("\t\t\t\t\t TRAIN SCHEDULE ");
  Railway.headingLine();
  System.out.println();
  System.out.println("\tNumber  Name \t\t\tStarting Stn  \t\tETD \tDestination Stn \tETA");
  System.out.println();
  int i1=0;
  for (i1=0; i1<=1;i1++)
   System.out.println("\t"+Railway.trno[i1]+"\t"+Railway.trnm[i1]+"\t"+Railway.trst[i1]+"\t"+Railway.deptm[i1]+"\t"+Railway.trds[i1]+"\t"+Railway.arrtm[i1]);
  System.out.println();
  System.out.println();
  Railway.pressKey();
 }
}