using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	// use once
	void Start ()
	{
		// loop
        	while(i < 6)
        	{
                	// things to do;
                	Debug.Log("the value of i " + i);
                	i++;
        	}
	}

	// update is called once per frame
	void Update ()
	{

	}

	// while loop
	while(i < 6)
	{
		// things to do;
		Debug.Log("the value of i " + i);
		i++;
	}

	// for loop
	for(var init; condition; inrement)
	{
		// things to do;
	}
}
