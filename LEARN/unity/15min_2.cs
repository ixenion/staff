// spawn objects
// create empty objet, rename to SpawnPoint
// reate another empty object, name it GameManager
// create GameController.cs script
// save spawn object as prefab
// to do this just create prefab folder and drag and drop spawnobject
using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	public GameObjet ball;
	public transform spawnPoint;
	
	public float maxX;
	public float maxZ;

	// use once
	void Start ()
	{
		// just spawn all
		//SpawnBall();

		// invoke repeating
		// spawn ball with 1 sec delay and 2 sec. repeat delay
		InvokeRepeating("SpawnBall", 1f, 2f);
	}

	// update is called once per frame
	void Update ()
	{
		// spawn ball by key event
		if (Input.GetkeyDown(KeyCode.Space))
			SpawnBall();
		// spawn a ball at any point where mouse clicks
		if (Input.GetMouseButtonDown(0))
		{
			Vector3 mousePos = Input.mousePosition;
			mousePos.z = 10f;
			Vector3 spawnpos = Camera.main.ScreenToWorldPoint(mousePos);
			Instantiate(ball, spawnPos, Quaternion.identity);
		}
	}

	void SpawnBall()
	{
		// Quaternion.identity means zero rotation by default?
		// every spawn at the same spot
		Instantiate(ball, spawnPoint.position, Quaternion.identity);// object to spawn, position, rotation.
	}

	void SpawnBallRandomly()
        {
                // Quaternion.identity means zero rotation by default?
                // every spawn at the random spot
		float randomX = Random.Range(-maxX,maxX);
		float randomZ = Random.Range(-maxZ,maxZ);
		Vector3 randomSpawnPos = new Vector3(randomX, 10f, randomZ);
                Instantiate(ball, randomSpawnPos, Quaternion.identity);// object to spawn, position, rotation.
        }

	void OnCollisionEnter(Collision collision)
	{
		GetComponent<Renderer>().materiall.color = Color.red;
	}
}
