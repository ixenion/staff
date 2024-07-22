// also we can access scipt from another sript

using UnityEngine;
using System.Colletions;

public class Test1 : MonoBehaviour
{
	// to acccess rigidbody component
	Rigidbody rb;
	// to access Box Collider component
	BoxCollider bc;
	// access to another script
	Test2 t2;// Test2 is public class of the script which access to
	// use once
	void Start ()
	{
		bc = GetComponent<BoxCollider>();
		// gives acess to rigid body attached to and stores inside rb var.
		rb = GetComponent<Rigidbody>();
		rb.velocity = new Vector3 (1,0,0);
		
		// get acess to "variab" variable which stored inside Test2 script
		t2 = GetComponent<Tets2>();
		Debug.Log(t2.variab)
	}

	// update is called once per frame
	void Update ()
	{

	}
}
