using System;

namespace Variales
{
	class Program
	{
		static void Main(string[] args)
		{
			byte number = 0;
			int count = 10;
			float totalPrice = 20.95f;
			char character = 'A';
			string firstName = "Mosh";
			bool isWorking = false;
			var b = 2;// type autodetect

			Console.WriteLine(number);
			Console.WriteLine(count);
			Console.WriteLine(totalPrice);
			Console.WriteLine(character);
			Console.WriteLine(firstName);
			Console.WriteLine(isWorking);
		}
	}
}
