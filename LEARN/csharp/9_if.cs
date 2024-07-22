using System;


namespace Decisions
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Bob's giveaway");
			Console.Write("Choose a door: 1, 2, or 3: ");
			string userValue = Console.ReadLine();
			
			if (userValue == "1")
			{
				string message = "You won a new acr!";
				Console.WriteLine(message);
			}
			else if (userValue == "2")
			{
				string message = "You won a new boat!";
				Console.WriteLine(message);
			}
			else if (userValue == "3")
			{
				string message = "You won a cat!";
				Console.WriteLine(message);
			}
			else
			{
				string message = "Invalid";
				Console.WriteLine(message);
			}
			Console.ReadLine();
		}
	}
}
