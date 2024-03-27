using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	public GameObject ball;
	public float speed;
	// use once
	void Start ()
	{
				
	}

	// update is called once per frame
	void Update ()
	{
		// keyboard input
		if (Input.GetKeyDown(KeyCode.Space)){
			inst();
		}
		// edit -> project settings -> input
		// here is why space attached to Jump
		if (Input.GetButtonDown("Jump")){
			Debug.Log("Space pressed");
			// mouse position
                	Vector3 mousePos = Input.mousePosition;
                	Debug.Log (mousePos.x);//x,y,z
		}

		// mouse button
		if (Input.GetMouseButtonDown (0)){
			DebugLog ("Left mouse butt pressed");
		}
		if (Input.GetMouseButtonDown (1)){
                        DebugLog ("Right mouse butt pressed");
                }
		if (Input.GetMouseButtonDown (2)){
                        DebugLog ("Mouse wheel pressed");
                }
		
		float x = Input.GetAxis ("Horizontal");
		float y = Input.GetAxis ("Vertical");
		// to move object
		transform.Translate(x*Time.deltaTime*speed,y*Time.deltaTime*speed,0);
	}

	void inst(){
		Instantiate(ball, transform.position, transform.rotation);
	}
}
