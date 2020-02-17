describe('Testing nav overlay open ', () => {

    it ('openSearchBar should increase width to 100%', function() {
        $(".content").append("<div id='overlaySearchBar' style='width:10%'></div>");
        let searchBar = document.getElementById("overlaySearchBar");
        expect(searchBar.style.width).toEqual('10%')
        openSearchBar();
        expect(searchBar.style.width).toEqual('100%')
    });
    
});

describe('Testing nav overlay close ', () => {

    it ('openSearchBar should decrease width to 0%', function() {
        $(".content").append("<div id='overlaySearchBar' style='width:100%'></div>");
        let searchBar = document.getElementById("overlaySearchBar");
        expect(searchBar.style.width).toEqual('100%')
        closeSearchBar();
        expect(searchBar.style.width).toEqual('0%')
    });
    
});

describe('capitalizeString function', () => {
        
    it ('capitalizeString should capitalize the first letter of the elements content', function() {
        $(".content").append('<input id="capitalizeText" value="this should capitalize">');
        let text = document.getElementById("capitalizeText");
        capitalizeString('capitalizeText');
        expect(text.value).toEqual('This should capitalize')
    });

});