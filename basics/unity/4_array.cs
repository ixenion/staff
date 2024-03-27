using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	// init array
	int[] a = {0,1,2,3,4,5,6};
	int[] b; // dynamic array?
	// become available in Inspector
	public int[] c;

	// use once
	void Start ()
	{
		Debug.Log(a[0]);
		b = new int[5]; // resize b array to 5 index
		// fill in array
		b[0] = 3;
		b[1] = 9;
		
		// for i in init - python analog
		foreach(int i in a)
		{
			Debug.Log(i);
		}

	}

	// update is called once per frame
	void Update ()
	{

	}
}
