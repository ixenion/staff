// get component in children function
using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	Rigidbody rb;
	// use once
	void Start ()
	{
		
	}

	// update is called once per frame
	void Update ()
	{
		// move children object while this script attahed to the main objectt
		rb = GetComponentInChildren<Rigidbody>();
		rb.velosity = new Vector3(1,0,0);
	}
}
