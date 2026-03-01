# Configuring SonarQube for IDE in PyCharm

To integrate SonarQube into PyCharm, you will use the official JetBrains plugin, which was formerly known as SonarLint but is now officially named **SonarQube for IDE**. 

Here are the complete steps to install, configure, and use it effectively.

## Step 1: Install the Plugin

1. Open PyCharm and go to **File > Settings** (or **PyCharm > Settings** on macOS).
2. Navigate to **Plugins** in the left-hand menu.
3. Select the **Marketplace** tab and search for **SonarQube for IDE** (or *SonarLint*).
4. Click **Install**.
5. Click **Restart IDE** when prompted to activate the plugin.

## Step 2: Configure the Connection (Connected Mode)

To ensure your IDE uses the exact same rules, quality gates, and exclusions as your team's central server, you need to connect the plugin to your SonarQube server.

1. Go back to **File > Settings > Tools > SonarQube for IDE**.
2. Click the **+ (Add)** button under the connections section to open the wizard.
3. Select **SonarQube Server** (or SonarQube Cloud if you are using the cloud version).
4. Enter a recognizable **Connection Name** and your **Server URL** (e.g., `http://localhost:9000`).
5. Provide a User Token. If you don't have one, click the **Create Token** button, which will redirect you to your SonarQube browser interface to generate it. Paste the token into PyCharm.
6. Click **Finish**, then click **OK** to save your new global connection.

## Step 3: Bind Your Project

Now that PyCharm is connected to the server, you need to tell it which local project corresponds to which remote project.

1. Navigate to **File > Settings > Tools > SonarQube for IDE > Project Settings**.
2. Check the box that says **Bind project to SonarQube Server / SonarCloud**.
3. Select the connection you just created from the dropdown menu.
4. In the **Project key** field, click **Search in list...** and choose your project's name as it appears on the SonarQube server.
5. Click **Apply** and **OK**.

## Step 4: How to Use SonarQube for IDE

Once everything is bound, the tool works continuously in the background to analyze your Python scripts.

* **On-the-fly Analysis:** As you type, the plugin functions like a real-time spell-checker. It underlines bugs, security vulnerabilities, and code smells directly in the editor using squiggly lines.
* **Quick Reviews:** Hover your cursor over the underlined code to see a brief tooltip describing the issue, often accompanied by a quick-fix suggestion.
* **Detailed Tool Window:** Open the **SonarQube for IDE** panel located at the bottom of the PyCharm interface. This window gives you a comprehensive breakdown of the issue, explains why the code is non-compliant, and shows the exact rule it violates.
* **Manual Scans:** To manually trigger an analysis on a specific file or a whole directory, right-click the item in your Project Explorer and select **Analyze > Analyze File with SonarQube** (or use the shortcut `Ctrl+Shift+S` / `Cmd+Shift+S`).