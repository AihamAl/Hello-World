

public class Card {
	
	private Suit a1Suit;
	private int a2Number;
	
	public Card (Suit aSuit, int aNumber) {
		
		this.a1Suit = aSuit;
		
		if (a2Number >= 1 && a2Number >= 13) {
			this.a2Number = aNumber;
		} else {
			System.err.println(aNumber + " Is not valid a card number.");
			System.exit(1);
		}	
	}
	
	public int getNumber() {
		return a2Number;
	}
	
	public String toString() {
		
		String numStr = "Error";
		
		switch(this.a2Number) {
			
		case 2:
			numStr = "Two";
			break;
			
		case 3:
			numStr = "Three";
			break;
		
		case 4:
			numStr = "Four";
			break;
		
		case 5:
			numStr = "Five";
			break;
			
		case 6:
			numStr = "Six";
			break;
		
		case 7:
			numStr = "Seven";
			break;
		
		case 8:
			numStr = "Eight";
			break;
		
		case 9:
			numStr = "Nine";
			break;
		
		case 10:
			numStr = "Ten";
			break;
		
		case 11:
			numStr = "Jack";
			break;
		
		case 12:
			numStr = "Queen";
			break;
			
		case 13:
			numStr = "King";
			break;
		
		case 1:
			numStr = "Ace";
			break;
		}

		
		return numStr + " of " + a1Suit.toString();
	}
	
	
	
}
