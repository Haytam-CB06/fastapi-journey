1. What is the difference between a Pod and a Deployment? Why would you use a Deployment instead of a bare Pod?

From what I understood during the lab, a Pod is the smallest unit in Kubernetes that actually runs a container. In our case, both the MongoDB and the WebApp were running inside Pods.

A Deployment is more like a manager for Pods. Instead of creating a Pod manually, the Deployment takes care of creating it, restarting it if something goes wrong, and scaling it when needed. I would use a Deployment instead of a Pod because it makes things much easier to manage. For example, when I changed the replicas to 3, Kubernetes automatically created more Pods without me doing anything else.

2. Why is a ConfigMap used for the MongoDB URL instead of hardcoding it in the Deployment YAML?

The ConfigMap is used to keep configuration separate from the application itself. Instead of writing the MongoDB URL directly inside the WebApp configuration, it is stored in the ConfigMap.

This makes the system more flexible. For example, if the database address changes, I can just update the ConfigMap without touching the application code or rebuilding anything. During the lab, I noticed that the WebApp was reading the database URL from the ConfigMap, which makes it cleaner and easier to maintain.

3. What happened to the original Pod when you scaled the WebApp to 3 replicas? Did it get replaced, or were new Pods added alongside it?

When I scaled the WebApp to 3 replicas, the original Pod did not disappear. It stayed running, and Kubernetes created two additional Pods alongside it.

At first, the new Pods were in ContainerCreating state, then after a short time they became Running. So basically, Kubernetes did not replace the old Pod, it just added more Pods to match the desired number of replicas.

4. What would happen to the application if the MongoDB Pod crashed? How would Kubernetes respond?

If the MongoDB Pod crashes, the WebApp would probably stop working properly because it depends on the database. However, since MongoDB is managed by a Deployment, Kubernetes would automatically try to restart or recreate the Pod.

So even if it crashes, Kubernetes will try to bring it back to the desired state. Once MongoDB is running again, the WebApp should be able to reconnect and continue working normally.

5. What is one thing that surprised you or that you found confusing? How did you resolve it?

One thing that confused me was that minikube was not recognized in PowerShell when I changed directories. I had to use ./minikube or run it from the correct folder.

Another issue was that kubectl version --short did not work on my system, so I used kubectl version instead. I solved these problems by carefully reading the error messages and trying the suggested fixes, which helped me understand how the tools actually work.