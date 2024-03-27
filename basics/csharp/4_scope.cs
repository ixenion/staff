{//all three vars acessable here
	byte a = 1;
	{// only b & c vars acessable in this block
		byte b = 2;
		{// c var only
			byte c = 3;
		}
	}
}
// None vars are available here
