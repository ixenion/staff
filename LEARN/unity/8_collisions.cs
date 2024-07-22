using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	// use once
	void Start ()
	{
		
	}

	// update is called once per frame
	void Update ()
	{

	}
	// for 2D collis. if 3D just "OnCollisionEnter"
	void OnCollisionEnter2D(Collision2D col)
	{
		Debug.Log("Collision");
		if(col.gameObject.tag == "someTag")
			Destroy (col.gameObject);// to destroy the object with whih gameObject collided
			Destroy (gameObject); // the gameObject
	}
}
