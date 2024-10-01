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

close_count: int = 0
for i in code.split("\n"):
    i = i.strip(" ")
    if i and i[0] == '}':
        close_count += 1
    pgi.write(i + '\n')

for j in range(close_count * 5):
    pgi.hotkey('ctrl', 'delete')
time.sleep(2)