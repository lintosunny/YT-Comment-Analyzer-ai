chrome.action.onClicked.addListener(async (tab) => {
    if (chrome.sidePanel) {
        await chrome.sidePanel.open({ tabId: tab.id });
    } else {
        console.error("Side panel API is not available.");
    }
});
