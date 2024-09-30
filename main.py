import pyautogui as pgi
import time

print("Please open the tab you want to paste the text into. The text will be pasted in 5 seconds...")
time.sleep(5)

# ! type code here

code = '''
import java.util.Scanner;

interface AgeCalculator {
    void printAge(int year);
}

class HumanAgeCalculator implements AgeCalculator {
    public void printAge(int year) {
        System.out.println("You are " + (2024 - year) + " years old.");
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int year = sc.nextInt();
        
        HumanAgeCalculator hc = new HumanAgeCalculator();
        
        hc.printAge(year);
    }
}'''

pgi.write(code)
time.sleep(2)