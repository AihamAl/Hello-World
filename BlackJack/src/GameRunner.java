import java.util.Scanner;

public class GameRunner {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		Deck theDeck = new Deck(1, true);
		
		
		Player me = new Player("Aiham");
		Player dealer = new Player("Dealer");
		
		
		me.addCard(theDeck.dealNextCard());
		dealer.addCard(theDeck.dealNextCard());
		me.addCard(theDeck.dealNextCard());
		dealer.addCard(theDeck.dealNextCard());
		
		
		System.out.println("Cards are dealt\n");
		me.printHand(true);
		dealer.printHand(false);
		System.out.println("\n");
		
		
		boolean meDone = false;
		boolean dealerDone = false;
		String ans;
		
		
		while(!meDone || !dealerDone) {
			
			System.out.print("Hit or Stay  (Enter H or S): ");
			ans = sc.next();
			System.out.println();
			
			
			
			 /* 
			  * 
			  * Jag tog hjälp från youtube.com, compareToIgnoreCase fungerade där men inte här!
			  * Annars ska spelet fungera! 
			  * */
			if(ans.compareToIgnoreCase("H") = 0) {
				
				meDone = !me.addCard(theDeck.dealNextCard());
			}
			
			else {
				meDone = true;
			}				
		}
		
		if(!dealerDone) {
			if(dealer.getHandSum() < 17) {
				System.out.println("The Dealer hits\n");
				dealerDone = !dealer.addCard(theDeck.dealNextCard());
				dealer.printHand(false);
			}
			
			else {
				System.out.println("The Dealer Stays\n");
				dealerDone = true;
			}
			
			System.out.println();
		}
			
		sc.close();
		
		
		me.printHand(true);
		dealer.printHand(true);
		
		
		int mySum = me.getHandSum();
		int dealerSum = dealer.getHandSum();
		
		if (mySum > dealerSum && mySum <= 21 || dealerSum > 21) {
			System.out.println("Your win!");
		}
		
		else {
			System.out.println("Dealer wins!");
		}
		
	}

}
