package test;

import java.awt.EventQueue;
import java.awt.GridLayout;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FilenameFilter;
import java.io.IOException;
import java.io.InputStream;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.SwingWorker;

import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.advanced.AdvancedPlayer;
import javazoom.jl.player.advanced.PlaybackEvent;
import javazoom.jl.player.advanced.PlaybackListener;

public class Launcher {

	private JFrame frame;
	private JPanel container;
	private List<String> songs = new ArrayList<String>();
	private int lastPlayIndex = -1;
	private Mp3Player mp3Player = null;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Launcher window = new Launcher();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Launcher() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		container = new JPanel();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JMenuBar menuBar = new JMenuBar();
		frame.setJMenuBar(menuBar);

		JMenu mnFile = new JMenu("File");
		menuBar.add(mnFile);

		JMenuItem mntmLoad = new JMenuItem("Load");
		mnFile.add(mntmLoad);

		JMenuItem mntmExit = new JMenuItem("Exit");
		mnFile.add(mntmExit);

		JMenu mnPlay = new JMenu("Play");
		menuBar.add(mnPlay);

		JMenu mnHelp = new JMenu("Help");
		menuBar.add(mnHelp);

		GridLayout layout = new GridLayout(loadSongs(), 1, 0, 0);
		container.setLayout(layout);
		initUI(container);
		JScrollPane scrollPane = new JScrollPane(container,
				JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,
				JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		frame.getContentPane().add(scrollPane);
	}

	private void initUI(final JPanel container) {
		Row row = null;
		int size = this.songs.size();
		for (int i = 0; i < size; i++) {
			row = new Row(i + 1, this.songs.get(i));
			container.add(row.songName);
		}

		container.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JLabel label = (JLabel) container.getComponentAt(e.getPoint());
				play(Row.getId(label.getText()));
				super.mouseClicked(e);
			}
		});
	}

	private void play(int index) {
		if (mp3Player != null) {
			new StopThread(mp3Player).execute();
			while (!mp3Player.isStopped.get());
		}
		mp3Player = new Mp3Player(index);
		new PlayThread(mp3Player).execute();

	}

	private int loadSongs() {
		File songDir = new File(
				"/media/lee/b66bba2c-7ffc-4910-8b30-23890e9ee04e/lee/music/wuxia");
		File[] songs = songDir.listFiles(new FilenameFilter() {
			@Override
			public boolean accept(File dir, String name) {
				return name.toLowerCase().endsWith(".mp3");
			}
		});
		for (File song : songs) {
			this.songs.add(song.getAbsolutePath());
		}
		return this.songs.size();
	}

	static class Row {
		JLabel songName = null;
		static DecimalFormat decimalFormat = new DecimalFormat("0000");

		public Row(int id, String songName) {
			this.songName = new JLabel(getLabelName(id, songName));
		}

		private String getLabelName(int id, String songName) {
			return decimalFormat.format(id) + " : "
					+ songName.substring(songName.lastIndexOf("/") + 1);
		}

		static int getId(String labelName) {
			return Integer.parseInt(labelName.substring(0, 4));
		}

	}

	class PlayThread extends SwingWorker<Void, Void> {
		private Mp3Player mp3Player;

		public PlayThread(Mp3Player mp3Player) {
			this.mp3Player = mp3Player;
		}

		@Override
		protected Void doInBackground() throws Exception {
			this.mp3Player.play();
			return null;
		}
	}

	class StopThread extends SwingWorker<Void, Void> {
		private Mp3Player mp3Player;

		public StopThread(Mp3Player mp3Player) {
			this.mp3Player = mp3Player;
		}

		@Override
		protected Void doInBackground() throws Exception {
			this.mp3Player.stop();
			return null;
		}
	}

	class Mp3Player {
		private int index;
		private FileInputStream is = null;
		private AdvancedPlayer player = null;
		final AtomicBoolean isStopped = new AtomicBoolean(true);

		public Mp3Player(int index) {
			this.index = index;
		}

		public void stop() {
			System.out.println("stop");
			if (player != null) {
				System.out.println("start stop");
				player.stop();
				if (is != null) {
					try {
						is.close();
						isStopped.set(true);
						System.out.println("stopped");
					} catch (IOException e) {
						e.printStackTrace();
					}
				}
			}
		}

		public void play() {
			try {
				is = new FileInputStream(Launcher.this.songs.get(index));
				player = new AdvancedPlayer(is);
				isStopped.set(false);
				player.setPlayBackListener(new PlaybackListener() {
					@Override
					public void playbackFinished(PlaybackEvent event) {
						System.out.println(event.getFrame());
					}
				});
				player.play();
			} catch (JavaLayerException | FileNotFoundException e) {
				e.printStackTrace();
			}
		}

	}

}
