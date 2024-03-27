using System;

namespace Variales
{
	class Program
	{
		static void Main(string[] args)
		{
			try
			{
				var number = "1234";
				byte b = Convert.ToByte(number);

				Console.WriteLine(b);
			}
			catch (Exception)
			{
				Console.WriteLine("The number couldn't be converted to a byte.");
			}
		}
	}
}
