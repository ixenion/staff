using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	public float speed = 5f;
	Vector3 temp1;
	// use once
	void Start ()
	{
		// accsess omponent of transform field of the gameObject
		transform.position;
		transform.rotation;
		transform.localScale;
		// to store this things
		Vector3 pos = transform.position;
		Vector3 rot = transform.rotation;
		Vector3 scale = transform.localScale;
		// or
		float pos2 = transform.position.x;
		// to change positon
		tempPos = transform.position;
		tempPos.x += 5f;
		// and return this walue back to transform
		transform.position = tempPos;
		// but not like that
		transform.position.x += 5f;
	}

	// update is called once per frame
	void Update ()
	{
		// move game object
		transform.Translate (0, speed * Time.deltaTime, 0);
		// rotate object. how much per frame
		transform.Rotate(speed,0,0);
		// scaling gameObject
		temp1 = transform.localScale;
		// temp1.x += 1f;
		temp1.x += Time.deltaTime;
		transform.localScale = temp1;
	}
}
