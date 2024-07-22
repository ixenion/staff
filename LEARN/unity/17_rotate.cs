using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{	
	public float rotateSpeed;
	// use once
	void Start ()
	{
		
	}

	// update is called once per frame
	void Update ()
	{

	}

	private void FixedUpdate()
	{
		transform.Rotate(Vector3.up, rotateSpeed);
	}
}
